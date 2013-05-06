#subprocess.call(["/usr/bin/pdb", "dictionaryGrabber.py", "-o", "HE", "-d", "EN", "-f", "/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/texts/Bible_Genesis/EN/ch_1.html"], env={"PATH":"/usr/local/heroku/bin:/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/lib/jvm/java/bin: /usr/lib/Canopy:/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/pt_main"})
import requests
import re
from bs4 import BeautifulSoup
import argparse
import codecs
import os
import sys
sys.path.append("/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'pt_main.settings'
import books
from languages.models import Languages, Translations

#-t "Bible Genesis" -l EN -f "temp/Bible_Genesis_EN.txt" -d "Bible_Genesis"
parser = argparse.ArgumentParser (description="Build Database for Words in File")
parser.add_argument("--original", "-o", required=True, help="Original Language")
parser.add_argument("--definition", "-d", required=True, help="Definiton Language")
parser.add_argument("--file", "-f",  required=True, help="input file")


language_dictionaries = {
    'SQ': 1,       # Albanian
    'AR': 2,       # Arabic
    'BG':3,        # Bulgarian
    'CS':  4,       # Czech
    'FA':  5,       # Farsi
    'FR':  6,       # French
    'DE': 7,        # German
    'EL': 8,        # Greek
    'HU': 9,       # Hungarian
    'IT': 10,       # Italian
    'LV': 11,     # Latvian
    'PL': 12,     # Polish
    'PT': 13,     # Portuguese
    'RO': 14,     # Romanian
    'RU': 15,     # Russian
    'HR': 16,     # Croatian
    'SK': 17,     # Slovak
    'ES': 18,     # Spanish
    'SV': 19,     # Swedish
    'TR':20,      # Turkish
    'VI': 21,      # Vietnamese
    'YI': 22,      # Yiddish
    'EN': 23,    # English
    'ZH': 24,      # Chinese
    'HE': 25 ,     # Hebrew
}

def translateWordUsingMorfix_EN_2_HE(word):
    dictionary_request = "http://www.morfix.co.il/" + word 
    r = requests.get(dictionary_request)
    response_text = r.text
    soup = BeautifulSoup(response_text)

    definition_soup = soup.find_all('div' , {"class": "default_trans"})
    all_definitions= ""
    for definition in (definition_soup):
        all_definitions = all_definitions + ";; "+ unicode(definition.string)

    if (len(all_definitions) > 3):
        all_definitions = all_definitions [3:]
    return all_definitions

def translateWordUsingMorfix_EN_2_HE(word):
    dictionary_request = "http://www.morfix.co.il/" + word 
    print dictionary_request
    r = requests.get(dictionary_request)
    response_text = unicode(r.text)
    soup = BeautifulSoup(response_text)
    definition_soup = soup.find_all('div') # , {"class": "translation translation_he heTrans"})
    definition_soup = soup.find("div", {"class": "translation translation_he heTrans" })
#definition_soup = soup.find_all('div' , {"class":"translation translation_he heTrans"})
    all_definitions= ""
    print str(definition_soup)
    if (definition_soup != None):
        for definition in (definition_soup):
            all_definitions += unicode(definition)
    if (len(all_definitions) > 3):
        all_definitions = all_definitions [3:]
    return all_definitions


def translateWordUsingMorfix_HE_2_EN(word):
    dictionary_request = "http://www.morfix.co.il/" + word
    r = requests.get(dictionary_request)
    response_text = r.text
    soup = BeautifulSoup(response_text)

    definition_soup = soup.find_all('div' , {"class": "default_trans"})
    all_definitions= ""
    for definition in (definition_soup):
        all_definitions = all_definitions + ";; "+ definition.string

    if (len(all_definitions) > 3):
        all_definitions = all_definitions [3:]
    return all_definitions

def translateWordUsingLingvozone(from_lang, to_lang, word):
    from_lang_id = str(language_dictionaries[from_lang])
    to_lang_id = str(language_dictionaries[to_lang])
    dictionary_request="http://www.lingvozone.com/dictionary?action=translation_ajax&language_id_from=" + from_lang_id + "&language_id_to=" + to_lang_id + "&word=" + word
#    print dictionary_request

    r = requests.get(dictionary_request)
    response_text = r.text
    soup = BeautifulSoup(response_text)
    definition_soup = soup.find_all('a' , {"class": "black"})
    all_definitions= ""
    for definition in (definition_soup):
        all_definitions = all_definitions + ", "+ definition.string

    if (len(all_definitions) > 2):
        all_definitions = all_definitions [2:]
    return all_definitions

def is_untranslated(left,  right,  original):
    return not (Translations.objects.filter(fromLang=left, toLang=right,
                                       original="%s" % original).exists())


def  add_word_to_database(left,right,original,translation):
    dj_translation = Translations (
        fromLang=left, 
        toLang=right,
        original="%s" % original,
        definition="%s" % translation)
    dj_translation.save()


'''
        dj_translation = Translations (
            left, 
            right,
            original="%s" % tran[2],
            definition="%s" % tran[3])
        dj_translation.save()
'''


'''
    from_lang = Languages.objects.get( abbr="%s" % 
                                          left.lower())
    to_lang = Languages.objects.get (
                    abbr="%s" %  right.lower())
'''



def main():
    import pdb
    args=parser.parse_args()
    original=args.original
    definition=args.definition
    print original
    print definition

    oLang=Languages.objects.get(abbr=original.lower())
    dLang=Languages.objects.get(abbr=definition.lower())
    file=args.file

    input_file = codecs.open(file,  encoding='utf-8')
    output_file=codecs.open("/home/mitchell/DEVELOPERparalleltextDEVELOPER/paralleltext/texts/output.txt",  'a', encoding='utf-8')

    contents = input_file.read()
    contents = re.sub("<.*?>", "", contents)
    all_words = re.split("\s*", contents)
#    db_name = original + "_2_" + definition
    for word in (all_words):
        if ((re.match("[a-zA-Z]",  word)) and
            is_untranslated( oLang, dLang, word)):
            word = re.sub ("\s*", "", word)
            translation = translateWordUsingMorfix_EN_2_HE(word)
            add_word_to_database(oLang,dLang,word,translation)
            output_file.write("['%s', '%s', '%s', '%s']\n" % (original, definition, word, translation))
#            print original + " " + definition +" " +  word +" " + translation
#        translation = translateWordUsingLingvozone(original, definition, word)

#            print "INSERT IGNORE INTO %s (`original`, `definition`) VALUES (\'%s\', \'%s\')" % (db_name, word, translation)
            
        

if __name__ == '__main__':
    main()
'''
from_lang = str(language_dictionaries['EN'])
to_lang  = str(language_dictionaries['HE'])
word = "God"
dictionary_request="http://www.lingvozone.com/dictionary?action=translation_ajax&language_id_from=" + from_lang + "&language_id_to=" + to_lang + "&word_id=&word=" + word
r = requests.get(url)
response_text = r.text
soup = BeautifulSoup(response_text)
definition_soup = soup.find_all('a' , {"class": "black"})
for definition in (definition_soup):
    definition_string = definition.string
    print definition_string

'''
