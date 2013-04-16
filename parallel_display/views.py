# coding: utf-8
# views.py
""" 
This file is responsible for taking the two texts and 
displaying them in a parallel layout.

We need to generalize this function to take any two texts

localhost/parallel_display/Bible_Genesis/ch_1/ENHE/

    (1) ENHE is separated into "EN" and "HE"
    (2) We then look in

    .. (a) localhost/texts/Bible_Genesis/EN/ch_1.html for the left text
    .. (b) localhost/texts/Bible_Genesis/HE/ch_1.html for the right text

"""
import re
from django.shortcuts import render
from bs4 import BeautifulSoup
from ptext.views import strip_page
page = ""
    
def get_page(page):
    """
    This function grabs the page and turns it into a 
    beautiful soup.
    
    It is unclear to me whether we actually need a separate
    function for this.
    """
    soup = BeautifulSoup(open(page))
    return soup

def parse_html(filepath):
    """parse_html takes an html file path and strips
    all tags from it besides <p> tags. the <p> tags are added
    to a list. parse_html returns a joined list as a string"""
    page = str(get_page(filepath))
    p_tag_list = re.findall('<p.*?</p>' , page , re.DOTALL)
    p_tag_string = "" . join(p_tag_list)
    return p_tag_string

def pdisplay(request):
    """
    This function takes the two texts, parses them both,
    and inserts them into the right and left windows.
    
    Right now, it is too specific.  It must be made more general
    to include any two texts
    
    Importantly, we must pass along information here about  
    whether the text flows Right To Left or Left To Right
    """
    
    #GET variables initialization
    book = ""
    chapter = ""
    from_lang = ""
    to_lang = ""
    path1 = ""
    path2 = ""

    
    if request.method == "GET":
        if request.get_full_path() != "/parallel_display/":
            book = request.GET.get("book",'')
            chapter = request.GET.get('chapter','')
            from_lang = request.GET.get('from_language','')
            to_lang = request.GET.get('to_language','')
            path1 = "texts/"+book+"/"+from_lang+"/"+chapter+".html"
            path2 = "texts/"+book+"/"+to_lang+"/"+chapter+".html"
        else:
            path1 = "texts/Bible_Genesis/EN/ch_1.html"
            path2 = "texts/Bible_Genesis/HE/ch_1.html"

    page1 = strip_page(parse_html(path1))
    page2 = strip_page(parse_html(path2))
    
    return render (request, 
                   "ptext/popupDemo.html",
                   {'myTitle':'Demo', 'css_url':'popup.css', 
                    'text1':page1, 'text2':page2, 
                    'img_url':'Info.png', 
                    'text1Dir':'left',  'text2Dir':'right'})
