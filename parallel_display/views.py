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
from books.models import BookInfo,BookTranslation
from languages.models import Languages
from parallel_display.forms import Book, Texts
import re
import argparse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse 
from django.core.context_processors import csrf
from bs4 import BeautifulSoup
from ptext.views import strip_page
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
import pdb 
#pdb.set_trace()
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

def selectLang(request,book_from_form):
    #url = reverse('selectLang', args=(), kwargs={'book_from_form': selected_book})
    return render(request,'parallel_display/select_lang.html')

def parse_html(filepath):
    """parse_html takes an html file path and strips
    all tags from it besides <p> tags. the <p> tags are added
    to a list. parse_html returns a joined list as a string"""
    page = str(get_page(filepath))
    p_tag_list = re.findall('<p.*?</p>' , page , re.DOTALL)
    p_tag_string = "" . join(p_tag_list)
    return p_tag_string

def selectBook(request):
    book_list = []
    selected_book = ""
    form = Book()
    form2 = Texts()
    all_books = BookInfo.objects.all()
    for book in all_books:
        title= book.title
        title_regex = re.sub("_", " ",title)
        book_list.append((title,title_regex))
    selects = tuple(book_list)
    form.fields['book_dd'].choices = selects
    if request.method == "POST":
       selected_book = request.POST['book_dd']
       return selectLang(request,selected_book)

    return render(request,
                   "parallel_display/select_book.html",{'form':form})

def selectChapLang(request):
    form = Texts()
    chap_list = []
    lang_list = []






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
    right_header=''
    left_header=''
    form=Texts()
    path1 = "texts/Bible_Genesis/EN/ch_1.html"
    path2 = "texts/Bible_Genesis/HE/ch_1.html"
    page1 = strip_page(parse_html(path1))
    page2 = strip_page(parse_html(path2))
    form_test = Texts()
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user).username
    else:
        username = ''

    return render (request,
                   "ptext/popupDemo.html",
                   {'myTitle':'Demo', 'css_url':'parallel_display/popup.css',
                    'text1':page1, 'text2':page2,
                    'img_url':'parallel_display/Info.png',
                    'text1Dir':'left',  'text2Dir':'right','form':form_test,
                    'username': username,'right_header':right_header})

