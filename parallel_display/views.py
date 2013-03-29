# coding: utf-8
# views.py
from flask import request
from coreapp import app
import re

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

webpage = """ 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
	<head>
		<title>Parallel Text</title>
</head>
	<body>
	<h1 align="center">Genesis English/Hebrew</h1>
	<table border="2" width="100%">
		<tr>
			<td dir="ltr" style="vertical-align: top;">"""+parseHtml("ch_1_eng.txt")+"""</td>
			<td dir="rtl" style="vertical-align: top;">"""+parseHtml("ch_1_heb.txt")+"""</td>
		</tr>
	</table>
	</body>
</html>
"""


@app.route("/")
def index():
	return webpage 
 