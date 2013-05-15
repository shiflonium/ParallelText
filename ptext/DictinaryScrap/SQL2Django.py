'''
This set of functions converts html to django DB statements
'''
import re
import codecs
from Languages.models import Languages


FILE_OBJ = codecs.open("workfile.txt", "r", "utf-8")
FILE = FILE_OBJ.read()
MY_FILE = open('workfile.txt', 'w')




def he_2_en():
    '''
	This function convert html strings to django DB statements 
	(hebrew to english)
	'''
    arr = re.findall(r'VALUES \(.*?\'\)', FILE, re.DOTALL)

    for i in range (0, len(arr)):
        arr[i] = arr[i].replace('VALUES', '')
        arr[i] = re.sub(r'\(\'', '(original=\'', arr[i])
        arr[i] = re.sub(r'\, \'', ', defininion=\'', arr[i])
        arr[i] = re.sub(
        	r'\(original=','(fromLang=\'HE\', toLang=\'EN\', original=', arr[i])
        MY_FILE.write("a=Translations" + arr[i].encode('utf8') + "\na.save()\n")
    MY_FILE.close()

def abbr_table():
    '''
    This function converts text file with languages abbreviations to 
    django DB statements
    '''
    arr = re.findall(r'VALUES \(.*?\'\)', FILE, re.DOTALL)

    for i in range (0, len(arr)):
        arr[i] = re.sub(r'VALUES', '', arr[i])
        arr[i] = re.sub(r'\(\'', '(abbr= \'', arr[i])
        arr[i] = re.sub(r'\, \'', ', name= \'', arr[i])
        arr[i] = re.sub(r' \'\)', '\')', arr[i])
        MY_FILE.write('a=AvailLangs'+arr[i].encode('utf8')+'\na.save()\n')

def uppercase_abbr_in_database():
    '''
    Convert the abbreviations in the database to uppercasse
    '''
    length = Languages.objects.count()
    for i in range(1, length):
        abb = Languages.objects.get(langID=i)
        abb.abbr = str(abb.abbr).upper()
        abb.delete()
        abb.save()


if __name__ == '__main__':
	#abbrTable()
    uppercase_abbr_in_database()




