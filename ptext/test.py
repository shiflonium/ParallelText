'''This class designed to test the popups module. Later on it will be extended
   to test the dictionary functions as well
'''

import unittest
import urllib2
from bs4 import BeautifulSoup
import re


EN = BeautifulSoup(open("../texts/Bible_Genesis/EN/ch_1.html"))

class TestPText(unittest.TestCase):
    '''
    This class designed to test the popups module. Later on it will be extended
    to test the dictionary functions as well
    '''
    def setup(self):
        '''
	This sets up the test of thepopups
	'''
        self.html = BeautifulSoup(
        urllib2.urlopen (
            'http://127.0.0.1:8000/parallel_display/').read())


    def test_num_paragraphs(self):
        '''compare the number of paragrpahs 
	between the original file and the fetched page'''
        #paragraphs in EN
        parEN = re.findall(r'<p.*?</p>', str(EN), re.DOTALL)

        #paragraphs in self
        par_self = re.findall(r'<td.*?</td>', str(self.html), re.DOTALL)
        par_self = re.findall(r'<p.*?</p>', par_self[0], re.DOTALL)
        
        string_report = "Original file has {} paragraphs and self has {} paragraphs".format(
		len(parEN), len(par_self))
        self.assertEqual(len(parEN), len(par_self), string_report)



    def test_popups(self):
        ''' compare the number of words 
	between the original file and the fetched page '''
        #Make a long string from EN
        en_content = re.findall(r'<p.*?</p>', str(EN), re.DOTALL)
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


        #Make a long string from slef
        self_content = re.findall(r'<td.*?</td>', str(self.html), re.DOTALL)
        self_content = re.findall(r'<em>.*?\b[^\W]+\b.*?<br>', 
				  self_content[0], re.DOTALL)
        self_content = str(self_content).replace('\\t','')
        self_content = str(self_content).replace('\\n','')
        self_content = str(self_content).replace('\'','')
        self_content = ''.join(self_content)
        self_content = str(self_content).replace(',', '')
        self_content = self_content.split()


        s = "Original file has {} words and self has {} words".format(
        len(en_content), len(self_content))
        
        self.assertEqual(len(en_content), len(self_content), s)



if __name__ ==  '__main__':
    unittest.main()
