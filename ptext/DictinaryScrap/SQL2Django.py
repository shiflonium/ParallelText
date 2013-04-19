import re
import codecs
from ptext.models import AvailLangs

#fileObj = codecs.open("LangsAbbr/abbr.sql","r","utf-8");
#x = fileObj.read()
f=open('workfile.txt', 'w');

#f.write('#coding: utf-8\nfrom django.db import models\nfrom ptext.models import AvailLangs\n\n')



def HE_2_EN():
	a = re.findall(r'VALUES \(.*?\'\)',x,re.DOTALL)

	for i in range (0, len(a)):
		a[i] = a[i].replace('VALUES','')
		a[i] = re.sub(r'\(\'','(original=\'',a[i])
		a[i] = re.sub(r'\, \'',', defininion=\'',a[i])
		a[i] = re.sub(r'\(original=','(fromLang=\'HE\', toLang=\'EN\', original=', a[i])
		f.write("a=Translations"+a[i].encode('utf8')+"\na.save()\n")

	f.close()

def abbrTable():
	a = re.findall(r'VALUES \(.*?\'\)', x, re.DOTALL)
	for i in range (0,len(a)):
		a[i] = re.sub(r'VALUES', '', a[i])
		a[i] = re.sub(r'\(\'', '(abbr= \'', a[i])
		a[i] = re.sub(r'\, \'', ', name= \'', a[i])
		a[i] = re.sub(r' \'\)', '\')', a[i])
		f.write('a=AvailLangs'+a[i].encode('utf8')+'\na.save()\n')

def uppercaseAbbrInDatabase():
	length = AvailLangs.objects.count()
	for i in range(1,length):
		abb = AvailLangs.objects.get(langID=i)
		abb.abbr = str(abb.abbr).upper()
		abb.delete()
		abb.save()


if __name__ == '__main__':
	#abbrTable()
	#uppercaseAbbrInDatabase()




