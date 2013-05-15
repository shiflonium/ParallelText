"""
this is a unit test file for the search feature in parallel_display
"""
import unittest
import urllib2
from bs4 import BeautifulSoup
import os, sys
import re
import mechanize
sys.path.append('/home/2bz2/Desktop/pdisplay/paralleltext')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pt_main.settings'
from  books.models import BookInfo, BookTranslation





class TestPDSearch(unittest.TestCase):
    '''
    This class designed to test the search module (serach bar) inside parallel_display.
    '''
    def setUp(self):
        '''
        This sets up the test of the select book dropdown
        '''
        self.html = BeautifulSoup(urllib2.urlopen (
            'http://parallel-text.herokuapp.com/parallel_display/').read())


    def test_book_dropdown(self):
        '''
        checks that all books from DB
        are in the dropdown for select book
        '''
        books_from_db = BookInfo.objects.values_list('title', flat = True)
        options = re.findall(r'<option value="(.*?)"',
        str(self.html) , re.DOTALL)
        flag = False
        error = """Check that all books from DB really appears
        in dropdown for select books"""
        for i in range(0, len(books_from_db)):
            if books_from_db[i] in options:
                flag = True
            else:
                flag = False
            self.assertTrue(flag, error)

    def test_chap_form(self):
        """this is a unit test for the chapters dropdown to
        check that it is populated with the correct amount of chapters this
        can be done by comapring the number of chapters in the db book_for
        the selected book and then, comaring it with the actual number of
        chapters in the chapters' dropdown"""

        error_msg = """
        you have a different number of chapters
        in your dropdown than in your database
        """
        books_from_db = BookInfo.objects.values_list('chaps', flat = True)
        browser = mechanize.Browser()
        url = 'http://parallel-text.herokuapp.com/parallel_display/'
        browser.open(url)
        browser.select_form(name = 'book_form')
        browser.submit()
        self.html = browser.response().read()
        soup = BeautifulSoup(self.html)
        chapters_select = soup.findAll('select', id = "id_chapter_dd")
        num_of_chapters = re.findall(r'<option value="(.*?)"',
            str(chapters_select), re.DOTALL)
        int_chap_dd = len(num_of_chapters)
        int_chap_db = int(books_from_db[0])
        self.assertEqual(int_chap_db, int_chap_dd, error_msg)

        	

    def test_left_lang_form(self):
        """this is a unit test for the available left side languages dropdown
        to check that it is populated with the correct amount of languages
        this can be done by selecting a book from the database and then 
        selecting its available language and store those in a list. 
        after that we compare it with the actual number of languages
        we get from the dropdown which was populated from the database"""
        error_msg = """
        you have a different number of languages for the selected book
        in your dropdown than in your database
        """

        lang_choices = []
        browser = mechanize.Browser()
        url = 'http://parallel-text.herokuapp.com/parallel_display/'
        browser.open(url)
        browser.select_form(name = 'book_form')
        selected_book = str(browser.form['book_dd'][0])
        browser.submit()
        id_of_book = BookInfo.objects.filter(title = selected_book)
        all_translations = BookTranslation.objects.filter(
        book_id = int(id_of_book[0].id))
        for tran in all_translations:
            lang = tran.language_id
            lang_name = lang.name
            lang_choices.append(lang_name)
        self.html = browser.response().read()
        soup = BeautifulSoup(self.html)
        lang_select = soup.findAll('select', id = "id_left_lang_dd")
        num_of_langs = re.findall(r'<option value="(.*?)"',
            str(lang_select), re.DOTALL)
        self.assertEqual(len(num_of_langs), len(lang_choices), error_msg)

    def test_right_lang_form(self):
        """this is a unit test for the available right side languages dropdown
        to check that it is populated with the correct amount of languages
        this can be done by selecting a book from the database and then 
        selecting its available language and store those in a list. 
        after that we compare it with the actual number of languages
        we get from the dropdown which was populated from the database"""
        lang_choices = []
        error_msg = """
        you have a different number of languages for the selected book
        in your dropdown than in your database
        """
       
        
        browser = mechanize.Browser()
        url = 'http://parallel-text.herokuapp.com/parallel_display/'
        browser.open(url)
        browser.select_form(name = 'book_form')
        selected_book = str(browser.form['book_dd'][0])
        browser.submit()
        id_of_book = BookInfo.objects.filter(title = selected_book)
        all_translations = BookTranslation.objects.filter(
        book_id = int(id_of_book[0].id))
        for tran in all_translations:
            lang = tran.language_id
            lang_name = lang.name
            lang_choices.append(lang_name)
        self.html = browser.response().read()
        soup = BeautifulSoup(self.html)
        lang_select = soup.findAll('select', id = "id_right_lang_dd")
        num_of_langs = re.findall(r'<option value="(.*?)"',
            str(lang_select), re.DOTALL)
        self.assertEqual(len(lang_choices), len(num_of_langs), error_msg)


if __name__ ==  '__main__':
    unittest.main()