#!/usr/bin/python
'''
this module controls the popups for the applicaiton
'''
#from django.http import HttpResponse

#from django.shortcuts import render
#from bs4 import BeautifulSoup
import re
import json
import requests
import urllib

#def getPage(htmlPage):
#    soup = BeautifulSoup(open(htmlPage));
#    return soup

def remove_commas(my_list, val):
    return [value for value in my_list if value != val]


def strip_page(page):
    #page = getPage('texts/Bible_Genesis/EN/ch_1.html')    #Get html source
    #page = getPage(html)    #Get html source

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
