#!/usr/bin/python
'''
this module controls the popups for the applicaiton
'''
#from django.http import HttpResponse

#from django.shortcuts import render
#from bs4 import BeautifulSoup
import re
#import json
#import urllib
from ptext.models import HE_2_EN
from django.core.exceptions import ObjectDoesNotExist

#from django.db import models

class mydict(object):
    def __init__(self,_o, _d):
        self.o = _o
        self.d = _d
    def __iter__(self):
        for i in range(0,len(self.o)):
            yield self.o[i]
    def get_original(self, index):
        return x.o[index]
    def get_definition(self,index):
        return x.d[index]


def remove_commas(my_list, val):
    '''Rmoving commas from a whole list'''
    return [value for value in my_list if value != val]


def strip_page(page):
    '''Cleans all html code from the text and return a list 
    of every Word including <p> tags'''

    #STRIP TEXT
    plist = re.findall(r'<p.*?</p>', str(page), re.DOTALL)
    stripped_para_list = re.findall(r'>.*?</p>', str(plist), re.DOTALL)
    stripped_para_list = re.sub(r'\\\\n', ' ', str(stripped_para_list))
    stripped_para_list = re.sub(r'\\\\r', '', str(stripped_para_list))
    stripped_para_list = re.sub(r'</p>',  '|', str(stripped_para_list))
    stripped_para_list = re.sub(r'>',  ' <p> ', str(stripped_para_list))
    stripped_para_list = re.sub("\|",  ' </p> ', str(stripped_para_list))
    stripped_para_list = re.sub(r'\[',  '', str(stripped_para_list))
    stripped_para_list = re.sub(r'\]',  '', str(stripped_para_list))

    #While loop to create a clean list
    pos = 0
    text = list()
    text.append('')
    i = 0

    while (i<len(stripped_para_list)):
        if (stripped_para_list[i] != ' '):
            text[pos] = text[pos]+stripped_para_list[i]

        else:
            pos = pos+1
            text.append('')
        i = i+1

    #Clean text
    text = remove_commas(text, '\'')
    text = remove_commas(text, '')
    text = remove_commas(text, '\', ')
    text = remove_commas(text, '"')
    text = remove_commas(text, '", ')
    text = remove_commas(text, "',")
    text = remove_commas(text, '",')


    #Enocde text to html
    for i in range (0, len(text)):
        text[i] = text[i].decode('string_escape')
        text[i] = text[i].decode('string_escape')

    return text



def get_translated_list(list_to_translate):
    '''Strip the words in the list'''
    i = 0
    
    translated_list = list()
    

    for i in range(0, len(list_to_translate)):
        list_to_translate[i] = list_to_translate[i].replace(':','')
        list_to_translate[i] = list_to_translate[i].replace('.','')
        list_to_translate[i] = list_to_translate[i].replace(',','')
        list_to_translate[i] = list_to_translate[i].replace('-','')

        #get translation and put in a different list
        if (list_to_translate[i] == '<p>' or list_to_translate == '</p>'):
            translated_list.append(str(i))
        else:
            try:
                temp = HE_2_EN.objects.get(
                    original=list_to_translate[i].decode('utf8'))
                translated_list.append(temp.definition)
            except ObjectDoesNotExist:
                translated_list.append(str(i))

    

            
    return translated_list

    
