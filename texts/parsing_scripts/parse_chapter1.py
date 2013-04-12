# This Python file uses the following encoding: utf-8

''' 
this is for parsing the first chapter and outputting it
'''

import re
import codecs
import sys


BASEDIR = "../../"
TEXTDIR = BASEDIR + "texts/"
BIBLEDIR = TEXTDIR + "Bible_Genesis/"

LANGUAGES = [
    "AR" ,
    "EL",
    #    "English" : "EN",
    #   "Spanish" : "ES",
    #   "Hebrew" : "HE",
    "KO",
    "LA",
#    "PT",
     "RU",
    "TH",
     "UK"  ,
    "ZH",
    "ZHMINNAN", 
]


LANG_ABBREV_TO_FULL = {
    "AR" : "Arabic",
    "EL" : "Greek",
    "EN":     "English",
    "ES" : "Spanish",
    "HE":    "Hebrew",
    "KO" : "Korean",
    "LA" : "Latin",
    "PT" : "Portugese",
     "RU" : "Russian",
    "TH" : "Thai",
     "UK"  : "Ukranian",
    "ZH" : "Chinese",
    "ZHMINNAN": "Chinese-Minnan", 
}



def parse_chapter_1(lang):
    '''
    this processes chapter one for each language
    '''
    input_filename =  BIBLEDIR  + lang + "/ch_1.txt"
    output_filename = BIBLEDIR  + lang + "/ch_1.html"
    input_file = codecs.open(input_filename,  encoding='utf-8')
    output_file = open(output_filename, 'w')
    contents = input_file.read()
    para_sub = "qua~~!!!~~qua"
    contents=re.sub("\r\n", para_sub, contents)
    contents=re.sub("\n\r", para_sub, contents)
    contents=re.sub("\n", para_sub, contents)
    contents=re.sub("(%s){2,}" % para_sub ,"\n", contents)
    contents=re.sub(para_sub," ", contents)

    full_lang = LANG_ABBREV_TO_FULL[lang]
    output = u'''
<!DOCTYPE html> 
<html lang=”%s”>
  <head>
    <title> Genesis :  Chapter 1 (%s) </title>
  <head>
    <meta language="%s">
    <meta charset="utf-8">
  </head>
  <body class="%s">
''' % (lang, full_lang, lang, lang)

    lines= contents.split("\n")
    p_class="bodytext" + lang
    line_num=1


    for line in  (lines):
        print line
        if re.search("\w", line, re.UNICODE):     #  no blank lines
            output += "<p class=%s id=\"%d\">" % (p_class, line_num)
            output += line
            output += "</p>\n"
            line_num += 1
    output += "\n</body>\n</html>"

    output_file.write(output.encode('utf8'))

def main():
    '''
    this goes through each language and calls parse
    '''

    for lang in (LANGUAGES):
        print lang
        parse_chapter_1(lang)


for lang in (LANGUAGES):
    parse_chapter_1(lang)



if __name__ == 'main':
    print FOO
    print LANGUAGES
    main()




















'''
Input_Files = {
    "AR" :  BIBLEDIR  + Language_Prefixes["Arabic"] + "/" + "ch_1.txt",
    "EL"  : BIBLEDIR  + Language_Prefixes["Greek"] + "/" + "ch_1.txt",
    "KO" :  BIBLEDIR  + Language_Prefixes["Korean"] + "/" + "ch_1.txt",
    "LA" : BIBLEDIR  + Language_Prefixes["Latin"] + "/" + "ch_1.txt",
    "RU"  : BIBLEDIR  + Language_Prefixes["Russian"] + "/" + "ch_1.txt",
    "TH": BIBLEDIR  + Language_Prefixes["Thai"] + "/" + "ch_1.txt",
    "UK" : BIBLEDIR  + Language_Prefixes["Ukranian"] + "/" + "ch_1.txt",
    "ZH" :  BIBLEDIR  + Language_Prefixes["Chinese"] + "/" + "ch_1.txt",
    "ZHMINNAN" : BIBLEDIR  + Language_Prefixes["Chinese_Minan"] + "/" + "ch_1.txt",
}


f = codecs.open(ar_text,  encoding='utf-8')
all_file = f.read()
verses = re.findall(ar_start, all_file, re.MULTILINE)
o=open(ar_html, 'w')
for verse in (verses):
    1
    o.write(verse.encode('utf8'))

f = codecs.open(el_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(ko_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(la_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(ru_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(th_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(uk_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(zh_text,  encoding='utf-8')
all_file = f.read()
print all_file

f = codecs.open(zh_min_text,  encoding='utf-8')
all_file = f.read()
print all_file
'''


'''
PARAGRAPH_PATTERNS =  {
    "ZH" :   r"[\w].*?\r\n\r", #  r"^\s?^(\d*\s*.*?)$", #  "\b\s?\^\d+\s*(.*)",
    "ZHMINNAN" : r"[\w].*?\r\n\r", #   r"^\s?(\d*\s*.*?)$",#    "\b\s?\d+\.\s*",

    "UK":   r"[\w].*?\r\n\r", # r"^\s?(\d*\s*.*?)$",  # "\b\s?\^\d+\s*",
    "TH":  r"[\w].*?\r\n\r", # r"^\s?(\d*:\d*\s*.*?)$",   # "\b\s?\* \d:\ d+\s*",

    "RU":   r"[\w].*?\r\n\r", # r"^\s?(\d*\s*.*?)$",  # "\b\s?\^\d+\s*",
    "LA":  r"[\w].*?\r\n\r", # r"^\s?(\d*\s+\.\s*.*?)$",   #"\b\s?\d\.\s*",
 
   "KO":  r"[\w].*?\r\n\r", # r"^\s?(\d*\s*\..*?)$",   #"\b\s? \d+\.\s*",
    "EL":    r"([\w \t]*?(\n|\r\n|\l)?[\w \t]?)(\n|\r\n|\l)(\n|\r\n|\l)*",
#*?(\n?(\w| |\t)*?)+)
#r"[\w].*?\n\l", #r"^\s?(\w*'\s*.*?)$",
               #  r"^\s?(\w.*'\s*.*?)",
    "AR" :  r"[\w].*?\r\n\r"
    #"^\\s?(\\d*\\s*.*?)\n\n"," ,
#"^\\s?(\\d*\\s*.*?)\n\n",# ,  #"^\\s?(\\d*\\s*.*?)\n\n"," ,  #"^\\s?(\\d*\\s*.*?)\n\n",
}
'''
