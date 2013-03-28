#from django.http import HttpResponse

from django.shortcuts import render
from bs4 import BeautifulSoup
import string
import re

def getPage(htmlPage):
	soup = BeautifulSoup(open(htmlPage));
	return soup

def removeCommas(myList, val):
	return [value for value in myList if value!=val]


def popupDemo(request):
	page = getPage('texts/Bible_Genesis/EN/ch_1.html')	#Get html source

	#STRIP TEXT
	plist = parList = re.findall(r'<p.*?</p>',str(page.html),re.DOTALL)
	strippedParList = re.findall(r'>.*?</p>',str(plist),re.DOTALL)
	strippedParList = re.sub(r'\\n',' ',str(strippedParList))
	strippedParList = re.sub(r'\\r','',str(strippedParList))
	strippedParList = re.sub(r'</p>', '\|',str(strippedParList))
	strippedParList = re.sub(r'>', ' <p> ',str(strippedParList))
	strippedParList = re.sub(r'\|', ' </p> ',str(strippedParList))
	strippedParList = re.sub(r'\\', '',str(strippedParList))
	strippedParList = re.sub(r'\d\.', '',str(strippedParList))
	strippedParList = re.sub(r'\d', '',str(strippedParList))
	strippedParList = re.sub(r',', '',str(strippedParList))
	strippedParList = re.sub(r'"', '',str(strippedParList))
	strippedParList = re.sub(r'\'', '',str(strippedParList))
	strippedParList = re.sub(r'\[', '',str(strippedParList))
	strippedParList = re.sub(r'\]', '',str(strippedParList))
	strippedParList = re.sub(r'\'', '',str(strippedParList))
	

	#While loop to create a clean list
	pos=0
	test=list()
	test.append('')
	i=0
	
	while (i<len(strippedParList)):
		if (strippedParList[i]!=' '):
			test[pos] = test[pos]+strippedParList[i]
		
		else:
			pos = pos+1
			test.append('')
		i=i+1

		test = removeCommas(test,',')
		test = removeCommas(test,'\'')


	
	return render(request, 'ptext/popupDemo.html',{'myTitle':'Popup Demo', 'css_url':'popup.css',
		'text':test, 'img_url':'Info.png'}) 







