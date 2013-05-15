
'''This class designed to test the popups module. Later on it will be extended
   to test the dictionary functions as well
'''

import unittest
#import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException


LEFT = BeautifulSoup(open("../texts/Bible_Genesis/EN/ch_1.html"))


class TestPText(unittest.TestCase):
    '''
    This class designed to test the popups module. Later on it will be extended
    to test the dictionary functions as well
    '''

    def setUp(self):
        '''
        This sets up the test of thepopups
        '''
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.html = ""


    def test_num_paragraphs_left(self):
        '''
        compare the number of paragrpahs 
        between the original file and the fetched page
        '''
        #Getting the source code
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Read Books").click()
        combox = driver.find_element_by_id("id_book_dd")
        for option in combox.find_elements_by_tag_name("option"):
            if (option.text == 'Bible Bible Genesis'):
                option.click()
        

        driver.find_element_by_name("book_submit").click()
        combox = driver.find_element_by_id('id_left_lang_dd')
        for option in combox.find_elements_by_tag_name('option'):
            if (option.text == 'English'):
                option.click()

        combox = driver.find_element_by_id('id_right_lang_dd')
        for option in combox.find_elements_by_tag_name('option'):
            if (option.text == 'Hebrew'):
                option.click()

        
        driver.find_element_by_name("chap_lang_submit").click()
        
        self.html = driver.page_source#.encode('utf8')
        

        par_en = re.findall(r'<p.*?</p>', str(LEFT), re.DOTALL)

        #paragraphs in self

        par_self = re.findall(r'<table.*?/table>',
            self.html.encode('utf-8'),re.DOTALL)
        
        par_self = re.findall(r'<p.*?/p>', 
            par_self[1], re.DOTALL)
        
        string_report = '''Original file has {} paragraphs and 
            self has {} paragraphs'''.format(
                len(par_en), len(par_self))

        self.assertEqual(len(par_en), len(par_self), string_report)




    def test_popups(self):
        ''' 
        compare the number of words 
        between the original file and the fetched page 
        '''

        #Getting the source code
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Read Books").click()
        combox = driver.find_element_by_id("id_book_dd")
        for option in combox.find_elements_by_tag_name("option"):
            if (option.text == 'Bible Bible Genesis'):
                option.click()
        

        driver.find_element_by_name("book_submit").click()
        combox = driver.find_element_by_id('id_left_lang_dd')
        for option in combox.find_elements_by_tag_name('option'):
            if (option.text == 'English'):
                option.click()

        combox = driver.find_element_by_id('id_right_lang_dd')
        for option in combox.find_elements_by_tag_name('option'):
            if (option.text == 'Hebrew'):
                option.click()

        
        driver.find_element_by_name("chap_lang_submit").click()
        
        self.html = driver.page_source

        #Make a long string from EN
        en_content = re.findall(r'<p.*?</p>', str(LEFT), re.DOTALL)
        en_content = re.findall(r'>.*?</p>', str(en_content), re.DOTALL)
        en_content = str(en_content).replace('</p>','')
        en_content = en_content.decode('string_escape')
        en_content = en_content.decode('string_escape')
        en_content = str(en_content).replace('>','')
        en_content = str(en_content).replace('\'','')
        en_content = str(en_content).replace('\"','')
        en_content = str(en_content).replace('[','')
        en_content = str(en_content).replace(']','')
        en_content = str(en_content).replace('\\n','')
        en_content = str(en_content).replace('\\r','')
        en_content = str(en_content).replace(',', '')
        en_content = en_content.split()


        #Make a long string from self
        self_content = re.findall(r'<table.*?</table>', 
            self.html, re.DOTALL)
        self_content = re.findall(r'data-original-title=.*?data',
            self_content[0],re.DOTALL)

        string_report = '''Original file has {} words and self 
        has {} words'''.format(len(en_content), len(self_content))
        self.assertEqual(len(en_content), len(self_content), string_report)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ ==  '__main__':
    unittest.main()


