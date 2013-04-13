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




















