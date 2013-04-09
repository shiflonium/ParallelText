#from django.http import HttpResponse
"""
This module is used to demonstrate the popup for dictionaries
The entire module has to be eliminated and integrated into
the parallel_display module
"""
from django.shortcuts import render
from bs4 import BeautifulSoup
import re

def get_page(html_page):
    """
    This function gets the beautiful soup from a page
    It probably isn't necessary.
    Just call beautiful soup
    """
    soup = BeautifulSoup(open(html_page))
    return soup

def remove_commas(my_list, val):
    """
    This removes commas from a string
    Probably isn't necessary as a separate function
    """
    return [value for value in my_list if value != val]


def popup_demo(request):
    """
    This function iterates through every word in the page
    and creates a popup text for it
    
    This function needs to be integrated into the main 
    paralleldisplay function
    
    Also, you need to fill the popups with dicitonary lookups
    
    Look at issue # 64 on how to do this
    """
    page = get_page('texts/Bible_Genesis/EN/ch_1.html')    #Get html source

    #STRIP TEXT
    plist =  re.findall(r'<p.*?</p>', str(page.html), re.DOTALL)
    stripped_par_list = re.findall(r'>.*?</p>', str(plist), re.DOTALL)
    stripped_par_list = re.sub(r'\\n', ' ', str(stripped_par_list))
    stripped_par_list = re.sub(r'\\r', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'</p>', '\|', str(stripped_par_list))
    stripped_par_list = re.sub(r'>', ' <p> ', str(stripped_par_list))
    stripped_par_list = re.sub(r'\|', ' </p> ', str(stripped_par_list))
    stripped_par_list = re.sub(r'\\', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\d\.', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\d', '', str(stripped_par_list))
    stripped_par_list = re.sub(r',', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'"', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\'', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\[', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\]', '', str(stripped_par_list))
    stripped_par_list = re.sub(r'\'', '', str(stripped_par_list))
    

    #While loop to create a clean list
    pos = 0
    test = list()
    test.append('')
    i = 0
    
    while (i<len(stripped_par_list)):
        if (stripped_par_list[i]!=' '):
            test[pos] = test[pos]+stripped_par_list[i]
        
        else:
            pos = pos+1
            test.append('')
        i = i+1

        test = remove_commas(test,',')
        test = remove_commas(test,'\'')


    
    return render(request, 'ptext/popupDemo.html',
                {'myTitle':'Popup Demo', 'css_url':'popup.css',
                'text':test, 'img_url':'Info.png'}) 