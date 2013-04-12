# This Python file uses the following encoding: utf-8
'''
this is for constructing the raw text files
for the bible

#arabic , book
greek,   book
english,   book
spanish, book
hebrew, book
korean,  book 
latin, book 
portugese, book 
russian       book [править
    </w/index.php?title=%D0%91%D1%8B%D1%82%D0%B8%D0%B5&action=edit&section=1>]
    Глава 1

#thai,  book    [แก้ไข
    </w/index.php?title=%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%9B%E0%B8%90%E0%B8%A1%E0%B8%81%E0%B8%B2%E0%B8%A5/1&action=edit&section=1>]
    1

การทรงสร้าง


ukranian,     [ред.
    </w/index.php?title=%D0%91%D1%96%D0%B1%D0%BB%D1%96%D1%8F_(%D0%9E%D0%B3%D1%96%D1%94%D0%BD%D0%BA%D0%BE)/%D0%91%D1%83%D1%82%D1%82%D1%8F&action=edit&section=1>]
    Глава 1


chinese,       [编辑
    </w/index.php?title=%E8%81%96%E7%B6%93_(%E5%92%8C%E5%90%88%E6%9C%AC)/%E5%89%B5%E4%B8%96%E8%A8%98&action=edit&section=1>]
    第一章


  [ç¼–è¾‘
    </w/index.php?title=%E8%81%96%E7%B6%93_(%E5%92%8C%E5%90%88%E6%9C%AC)/%E5%89%B5%E4%B8%96%E8%A8%98&action=edit&section=1>]
    ç¬¬ä¸€ç« 



chinese minan

    [siu-kái
    </w/index.php?title=S%C3%A8ng-keng_(Kong-h%C5%8De)/Chh%C3%B2ng-s%C3%A8-k%C3%AC&action=edit&section=1>]
    Kòan 1


'''

import requests
from bs4 import BeautifulSoup
import codecs

def get_english():
    '''
    pulls down the english bible
    '''
    english_top = "http://en.wikisource.org/wiki/Bible_%28Jewish_Publication_Society_1917%29/Genesis#Chapter_1"
    page_data =  requests.get(english_top)
    english_text =  page_data.text
#    f = open('english.html', 'w')
#    f.write(english_text.encode('utf8'))
    divide_entire_html_book_into_chapters(
        arabic_text, 
        start_book_delimiter, 
        end_book_delimiter,
        start_chapter_delimiter,
        end_chapter_delimiter, 
        start_paragraph_delimiter,
        end_paragraph_delimiter)


def get_spanish():
    '''
    pulls down the thai bible
    '''
    spanish_top = "http://es.wikisource.org/wiki/Génesis:_Capítulo_1"
    page_data = requests.get(spanish_top)
    spanish_text =  page_data.text



def get_hebrew():
    '''
    pulls down the thai bible
    '''
    hebrew_top = "http://he.wikisource.org/wiki/בראשית_א" 
    page_data = requests.get(hebrew_top)
    hebrew_text =  page_data.text


def get_chinese_minnan():
    '''
    pulls down the thai bible
    '''
    chinese_minnan_top = "http://zh-min-nan.wikisource.org/wiki/Sèng-keng_(Kong-hōe)/Chhòng-sè-kì#K.C3.B2an_1" 
    page_data = requests.get(chinese_minnan_top)
    chinese_minnan_text =  page_data.text


def get_chinese():
    '''
    pulls down the thai bible
    '''
    chinese_top = "http://zh.wikisource.org/wiki/聖經_(和合本)/創世記#.E7.AC.AC.E4.B8.80.E7.AB.A0"
    page_data = requests.get(chinese_top)
    chinese_text =  page_data.text


def get_ukranian():
    '''
    pulls down the thai bible
    '''
    ukranian_top = "http://uk.wikisource.org/wiki/Буття#.D0.93.D0.BB.D0.B0.D0.B2.D0.B0_1"
    page_data = requests.get(ukranian_top)
    ukranian_text =  page_data.text
    divide_entire_html_book_into_chapters(
        arabic_text, 
        start_book_delimiter, 
        end_book_delimiter,
        start_chapter_delimiter,
        end_chapter_delimiter, 
        start_paragraph_delimiter,
        end_paragraph_delimiter)


def get_thai():
    '''
    pulls down the thai bible
    '''
    thai_top = "http://th.wikisource.org/wiki/พระธรรมปฐมกาล/1#1"
    page_data = requests.get(thai_top)
    thai_text =  page_data.text

def get_russian():
    '''
    pulls down the russian bible
    '''
    russian_top = "http://ru.wikisource.org/wiki/Бытие#.D0.93.D0.BB.D0.B0.D0.B2.D0.B0_1"
    page_data = requests.get(russian_top)
    russian_text =  page_data.text


def get_portugese():
    '''
    pulls down the portugese bible
    '''
    portugese_top = "http://pt.wikisource.org/wiki/Tradução_Brasileira_da_Bíblia/Gênesis/I"
    page_data = requests.get(portugese_top)
    portugese_text =  page_data.text
    get_chapter_per_html_page(
        arabic_text, 
        start_chapter_delimiter,
        end_chapter_delimiter, 
        start_paragraph_delimiter,
        end_paragraph_delimiter,
        next_chapter_iterator)



def get_korean():
    '''
    pulls down the korean bible
    '''
    korean_top = "http://ko.wikisource.org/wiki/창세기#1.EC.9E.A5"
    page_data = requests.get(korean_top)
    korean_text =  page_data.text

def get_latin():
    '''
    pulls down the latin bible
    '''
    latin_top = "http://la.wikisource.org/wiki/Liber_Genesis#1"
    page_data = requests.get(latin_top)
    latin_text =  page_data.text

def get_greek():
    '''
    pulls down the greek bible
    '''
    greek_top = "http://el.wikisource.org/wiki/Γένεσις#.CE.9A.CE.B5.CF.86.CE.AC.CE.BB.CE.B1.CE.B9.CE.BF.CE.BD_.CE.B1.27"
    page_data = requests.get(greek_top)
    greek_text =  page_data.text
    divide_entire_html_book_into_chapters(
        greek_text, 
        start_book_delimiter, 
        end_book_delimiter,
        start_chapter_delimiter,
        end_chapter_delimiter)

def get_arabic():
    '''
    pulls down the arabic bible
    '''
    arabic_top = "http://ar.wikisource.org/wiki/سفر_التكوين#.D8.B3.D9.81.D8.B1_.D8.A7.D9.84.D8.AA.D9.83.D9.88.D9.8A.D9.86_1"
    page_data = requests.get(arabic_top)
    arabic_text =  page_data.text
    divide_entire_html_book_into_chapters(
        arabic_text, 
        start_book_delimiter, 
        end_book_delimiter,
        start_chapter_delimiter,
        end_chapter_delimiter, 
        start_paragraph_delimiter,
        end_paragraph_delimiter)
# <h2><span class="editsection">[<a href="/w/index.php?title=%D8%B3%D9%81%D8%B1_%D8%A7%D9%84%D8%AA%D9%83%D9%88%D9%8A%D9%86&amp;action=edit&amp;section=24" title="حرر القسم: سفر التكوين 24">تعديل</a>]</span> <span class="mw-headline" id=".D8.B3.D9.81.D8.B1_.D8.A7.D9.84.D8.AA.D9.83.D9.88.D9.8A.D9.86_24">سفر التكوين 24</span></h2>


def divide_entire_html_book_into_chapters(    
        html_text, 
        start_book_delimiter, 
        end_book_delimiter,
        start_chapter_delimiter,
        end_chapter_delimiter):

    '''
    '''
    book_text = re.match(r"%s(.*)%s" 
                         %    start_book_delimiter, end_book_delimiter)    
    index = 1
    while chapter_text = re.match (
        start_book_delimiter,
        (.*),
        end_book_delimiter,
        re.DOTALL):
        chapter_file = "ch_" + str(index) + ".html"
        create_new_chapter(chapter_text)


def main():
    get_english()
    get_spanish()
    get_hebrew()
    get_chinese_minnan()
    get_chinese()
    get_ukranian()
    get_thai()
    get_russian()
    get_portugese()
    get_korean()
    get_greek()
    get_arabic()


if __name__ == '__main__':
    main()
