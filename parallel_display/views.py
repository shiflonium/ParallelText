# coding: utf-8
# views.py
import re
from django.shortcuts import render
from bs4 import BeautifulSoup
page=""
def getPage(page):
	soup=BeautifulSoup(open(page))
	return soup

def parseHtml(filepath):
	"""parseHtml takes an html file path and strips
	all tags from it besides <p> tags. the <p> tags are added
	to a list. parseHtml returns a joined list as a string"""
	page=str(getPage(filepath))
	pTagList=re.findall('<p.*?</p>',page,re.DOTALL)
	pTagString="".join(pTagList)
	return pTagString

def pdisplay(request):
	patheng="texts/Bible_Genesis/EN/ch_1.html"
	pathheb="texts/Bible_Genesis/HE/ch_1.html"
	eng_cell=parseHtml(patheng)
	heb_cell=parseHtml(pathheb)
	return render(request,"parallel_display/display.html",{'eng_text':eng_cell,'heb_text':heb_cell})