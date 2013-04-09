#from django.http import HttpResponse

from django.shortcuts import render
#from bs4 import BeautifulSoup
import string
import re

#def getPage(htmlPage):
#	soup = BeautifulSoup(open(htmlPage));
#	return soup

def removeCommas(myList, val):
	return [value for value in myList if value!=val]


def stripPage(page):
	#page = getPage('texts/Bible_Genesis/EN/ch_1.html')	#Get html source
	#page = getPage(html)	#Get html source

	#STRIP TEXT
	plist = re.findall(r'<p.*?</p>',str(page),re.DOTALL)
	strippedParList = re.findall(r'>.*?</p>',str(plist),re.DOTALL)
	strippedParList = re.sub(r'\\\\n',' ',str(strippedParList))
	strippedParList = re.sub(r'\\\\r','',str(strippedParList))
	strippedParList = re.sub(r'</p>', '|',str(strippedParList))
	strippedParList = re.sub(r'>', ' <p> ',str(strippedParList))
	strippedParList = re.sub("\|", ' </p> ',str(strippedParList))
	strippedParList = re.sub(r'\[', '',str(strippedParList))
	strippedParList = re.sub(r'\]', '',str(strippedParList))
	
	#While loop to create a clean list
	pos=0
	text=list()
	text.append('')
	i=0
	
	while (i<len(strippedParList)):
		if (strippedParList[i]!=' '):
			text[pos] = text[pos]+strippedParList[i]
		
		else:
			pos = pos+1
			text.append('')
		i=i+1

	#Clean text
	text = removeCommas(text,'\'')
	text = removeCommas(text,'')
	text = removeCommas(text,'\',')
	text = removeCommas(text,'"')
	text = removeCommas(text,'",')


	#Enocde text to html
	for i in range (0,len(text)):
		text[i]=text[i].decode('string_escape')
		text[i]=text[i].decode('string_escape')
		

	
	return text

#def popupDemo(request):
#	page1 = stripPage('texts/Bible_Genesis/EN/ch_1.html')
#	page2 = stripPage('texts/Bible_Genesis/HE/ch_1.html')
	
#	return render(request, 'ptext/popupDemo.html',{'myTitle':'Demo', 'css_url':'popup.css',
#		'text1':page1, 'text2':page2, 'img_url':'Info.png'}) 







