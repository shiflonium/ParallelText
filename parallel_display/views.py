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
from django.views.generic import TemplateView
import argparse
from django.shortcuts import render, redirect, render_to_response
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



def parse_html(filepath):
    """parse_html takes an html file path and strips
    all tags from it besides <p> tags. the <p> tags are added
    to a list. parse_html returns a joined list as a string"""
    page = str(get_page(filepath))
    p_tag_list = re.findall('<p.*?</p>' , page , re.DOTALL)
    p_tag_string = "" . join(p_tag_list)
    return p_tag_string

def selectLang(request,book_from_form,form):
    #url = reverse('selectLang', args=(), kwargs={'book_from_form': selected_book})
    lang_choices = []
    chap_choices = []
    chap_num = BookInfo.objects.filter(title = book_from_form)
    all_translations = BookTranslation.objects.filter(book_id = int(chap_num[0].id))
    for i in range(0,int(chap_num[0].chaps)):
        chap_choices.append(("ch_"+str(i+1),"Chapter "+str(i+1)))
    for tran in all_translations:
        lang = tran.language_id
        lang_name = lang.name
        lang_abbr = lang.abbr
        lang_choices.append((lang_abbr,lang_name))
    form.fields['chapter_dd'].choices = tuple(chap_choices)
    form.fields['right_lang_dd'].choices = tuple(lang_choices)
    form.fields['left_lang_dd'].choices = tuple(lang_choices)
    
def getLangName(book_name):
    id_of_book= BookInfo.objects.filter(title = book_name)
    all_translations = BookTranslation.objects.filter(book_id = int(id_of_book[0].id))
    for tran in all_translations:
        lang = tran.language_id
        lang_name = lang.name
        lang_abbr = lang.abbr
        lang_choices.append((lang_abbr,lang_name))



def selectBook(request):
    book_list = []
    selected_book = ""
    book_form = Book()
    lang_form = Texts()
    jj=[]
    #form2 = Texts()
    all_books = BookInfo.objects.all()
    for book in all_books:
        title= book.title
        title_regex = re.sub("_", " ",title)
        book_list.append((title,title_regex))
    selects = tuple(book_list)
    book_form.fields['book_dd'].choices = selects
    if request.method == "POST":
        if "book_submit" in request.POST:
            selected_book = request.POST['book_dd']
            request.session['jj'] = selected_book
            #print selected_book
            selectLang(request,selected_book,lang_form)
            #selectLang(request, selected_book, lang_form)
            #request.session['book_temp'] == selected_book
            book_title = re.sub("_", " ",selected_book)
            return render(request,'parallel_display/select_lang.html',{'form':lang_form,'book_header':book_title})
        if "chap_lang_submit" in request.POST:
            final_book = request.session.get('jj')
            #print lang_form.data['chapter_dd']
            print jj
            final_chapter = request.POST['chapter_dd']
            right = request.POST['right_lang_dd']
            left = request.POST['left_lang_dd']
            print selected_book
            path_right = "texts/%s/%s/%s.html" % (final_book, right.upper(), final_chapter)
            path_left = "texts/%s/%s/%s.html" % (final_book, left.upper(), final_chapter)
            page1 = strip_page(parse_html(path_right))
            page2 = strip_page(parse_html(path_left))
            if request.user.is_authenticated():
                username = User.objects.get(username=request.user).username
            else:
                username = ''
            return render (request,
                   "ptext/popupDemo.html",
                   {'myTitle':'Demo', 'css_url':'parallel_display/popup.css',
                    'text1':page1, 'text2':page2,
                    'img_url':'parallel_display/Info.png',
                    'text1Dir':'left',  'text2Dir':'right',
                    'username': username})

        
        #return HttpResponseRedirect(reverse('parallel_display.views.selectLang', args=(selected_book,)))
       #return reverse('selectLang', args=(), kwargs={'book_from_form': selected_book})


    return render(request,
                   "parallel_display/select_book.html",{'form':book_form})



def selectChapLang(request):
    form = Texts()
    chap_list = []
    lang_list = []






def pdisplay(request, final_book, chap, right, left):
    """
    This function takes the two texts, parses them both,
    and inserts them into the right and left windows.

    Right now, it is too specific.  It must be made more general
    to include any two texts

    Importantly, we must pass along information here about
    whether the text flows Right To Left or Left To Right
    """


    #GET variables initialization
    #book = ""
    #chapter = ""
    #from_lang = ""
    #to_lang = ""
    #path1 = ""
    #path2 = ""
    #right_header=''
    #left_header=''
    #form=Texts()
    #path1 = "texts/Bible_Genesis/EN/ch_1.html"
    path_right = "texts/book/right/chap.html"
    #path2 = "texts/Bible_Genesis/HE/ch_1.html"
    path_left = "texts/book/left/chap.html"
    page1 = strip_page(parse_html(path_right))
    page2 = strip_page(parse_html(path_left))
    #form_test = Texts()
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user).username
    else:
        username = ''

    return render (request,
                   "ptext/popupDemo.html",
                   {'myTitle':'Demo', 'css_url':'parallel_display/popup.css',
                    'text1':page1, 'text2':page2,
                    'img_url':'parallel_display/Info.png',
                    'text1Dir':'left',  'text2Dir':'right',
                    'username': username,'right_header':right_header})

