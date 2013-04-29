# This Python file uses the following encoding: utf-8

''' 
this is for parsing the first chapter and outputting it
'''

import re
import codecs
import sys
import argparse
import os

BASEDIR = "../../"
#BASEDIR = os.getcwd() + "/"
#TEXTDIR = BASEDIR + "texts/"

#-t "Bible Genesis" -l EN -f "temp/Bible_Genesis_EN.txt" -d "Bible_Genesis"
parser = argparse.ArgumentParser (description="Convert Book Text File to Html")
parser.add_argument("--title", "-t", required=True, help="title of the book")
parser.add_argument("--lang", "-l", required=True, help="language")
parser.add_argument("--file", "-f",  required=True, help="input file")
parser.add_argument("--dir", "-d",  required=True, help="output directory")

LANGUAGES = [
    "AR" ,
    "EL",
    "English" ,
    "Spanish",
    "Hebrew" ,
    "KO",
    "LA",
    "PT",
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
}




def convert_book_to_html (book_subdir, lang, book_name, book_text):
    lang=str(lang)
    dirname = os.path.dirname
    PROJECT_ROOT = dirname(dirname(os.path.realpath(__file__)))
    TEXT_DIR = os.path.join(PROJECT_ROOT, 'texts')
    output_dir = TEXT_DIR + "/" + book_subdir + "/" + lang + "/"
    if (os.path.exists(output_dir)==False):
              os.makedirs(output_dir)
     
    chapters=book_text.split("[Chapter]")
    chap_num=1
    for chapter in (chapters):
        if re.search("\w", chapter, re.UNICODE):     #  no blank chapters
            convert_chapter_to_html (output_dir, lang, book_name,
                                 chapter, chap_num)
            chap_num+=1

    
def convert_chapter_to_html (output_dir, lang, book_name,
                             chapter_text, chap_num):
    
    '''
    this processes each chapter for each language
    '''
    output_filename = output_dir + "ch_" + str(chap_num) + ".html"
    output_file = open(output_filename, 'w')


    para_sub = "qua~~!!!~~qua"
    contents = chapter_text
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
    <title> %s :  Chapter %d (%s) </title>
  <head>
    <meta language="%s">
    <meta charset="utf-8">
  </head>
  <body class="%s">
''' % (lang, book_name, chap_num, full_lang, lang, lang)

    lines= contents.split("\n")
    p_class="bodytext" + lang
    line_num=1


    for line in  (lines):
        if re.search("\w", line, re.UNICODE):     #  no blank lines
            output += "<p class=\"%s\" id=\"%d\">" % (p_class, line_num)
            output += line
            output += "</p>\n"
            line_num += 1
    output += "\n</body>\n</html>"

    output_file.write(output.encode('utf8'))

def main():
    '''
    this goes through each language and calls parse
    '''
    args=parser.parse_args()
    title=args.title
    lang=args.lang
    file=args.file
    dir=args.dir
    print title
    print lang
    print file
    print dir
    input_file = codecs.open(file,  encoding='utf-8')
    contents = input_file.read()
    convert_book_to_html (dir, lang, title, contents)


if __name__ == '__main__':
    main()




















