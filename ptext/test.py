import unittest
import urllib2
from bs4 import BeautifulSoup
import re

'''This class designed to test the popups module. Later on it will be extended
   to test the dictionary functions as well
'''

EN=BeautifulSoup(open("../texts/Bible_Genesis/EN/ch_1.html"))

class testPText(unittest.TestCase):
	def setUp(self):
		self.html=BeautifulSoup(urllib2.urlopen('http://127.0.0.1:8000/parallel_display/').read())


	'''compare the number of paragrpahs between the original file and the fetched page'''
	def testNumOfParagtaphs(self):
		#paragraphs in EN
		parEN = re.findall(r'<p.*?</p>',str(EN), re.DOTALL)

		#paragraphs in self
		parSelf = re.findall(r'<td.*?</td>',str(self.html),re.DOTALL)
		parSelf = re.findall(r'<p.*?</p>',parSelf[0], re.DOTALL)
		
		s = "Original file has {} paragraphs and self has {} paragraphs".format(len(parEN),len(parSelf))
		self.assertEqual(len(parEN),len(parSelf),s)


	''' compare the number of words between the original file and the fetched page '''
	def testPopups(self):
		#Make a long string from EN
		ENcontent = re.findall(r'<p.*?</p>',str(EN), re.DOTALL)
		ENcontent = re.findall(r'>.*?</p>',str(ENcontent), re.DOTALL)
		ENcontent = str(ENcontent).replace('</p>','')
		ENcontent = ENcontent.decode('string_escape')
		ENcontent = ENcontent.decode('string_escape')
		ENcontent = str(ENcontent).replace('>','')
		ENcontent = str(ENcontent).replace('\'','')
		ENcontent = str(ENcontent).replace('\"','')
		ENcontent = str(ENcontent).replace('[','')
		ENcontent = str(ENcontent).replace(']','')
		ENcontent = str(ENcontent).replace('\\n','')
		ENcontent = str(ENcontent).replace('\\r','')
		ENcontent = str(ENcontent).replace(',','')
		ENcontent = ENcontent.split()


		#Make a long string from slef
		selfContent = re.findall(r'<td.*?</td>',str(self.html), re.DOTALL)
		selfContent=re.findall(r'<em>.*?\b[^\W]+\b.*?<br>',selfContent[0],re.DOTALL)
		selfContent = str(selfContent).replace('\\t','')
		selfContent = str(selfContent).replace('\\n','')
		selfContent = str(selfContent).replace('\'','')
		selfContent = ''.join(selfContent)
		selfContent = str(selfContent).replace(',','')
		selfContent = selfContent.split()


		s = "Original file has {} words and self has {} words".format(len(ENcontent),len(selfContent))
		
		self.assertEqual(len(ENcontent),len(selfContent),s)



if __name__ == '__main__':
	unittest.main()