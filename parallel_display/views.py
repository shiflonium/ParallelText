# coding: utf-8
# views.py
import re
from django.shortcuts import render
page=""
def parseHtml(filepath):
	"""parseHtml takes an html/text file path and strips
	all tags from it besides <p> tags. the <p> tags are added
	to a list. parseHtml returns a joined list as a string"""
	f=open(filepath,"r")
	initialList=f.readlines()
	listAsString="".join(initialList)
	pTagList=re.findall('<p.*?</p>',listAsString,re.DOTALL)
	pTagString="".join(pTagList)
	f.close()
	return pTagString

def pdisplay(request):
	patheng="/home/2bz2/Desktop/pdisplay/paralleltext/parallel_display/ch_1_eng.txt"
	pathheb="/home/2bz2/Desktop/pdisplay/paralleltext/parallel_display/ch_1_heb.txt"
	eng_cell=parseHtml(patheng)
	heb_cell=parseHtml(pathheb)
	print eng_cell
	return render(request,"parallel_display/display.html",{'eng_text':eng_cell,'heb_text':heb_cell})