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
from books.models import BookInfo
from django.shortcuts import render
from django.core.context_processors import csrf
from bs4 import BeautifulSoup
from ptext.views import strip_page
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

page = ""


left_lang = (
        ("en","English"),
        ("he","Hebrew"),
        ("el","Greek"),
        ("es","Spanish"),
        ("pt","Portuguese"),
        ("ru","Russian"),
        ("ar","Arabic"),
        )

right_lang = (
        ("en","English"),
        ("he","Hebrew"),
        ("el","Greek"),
        ("es","Spanish"),
        ("pt","Portuguese"),
        ("ru","Russian"),
        ("ar","Arabic"),
        )



class Search(forms.Form):
    book_dd = forms.CharField(label="Search Book")

class Texts(forms.Form):
    b=BookInfo.objects.filter(title="Quran")
    chap_num_str=b[0].chaps
    chap_num=int(chap_num_str)
    chap_choices=[]
    for i in range (1,chap_num):
        chap_choices.append(("ch_"+str(i),"Chapter "+str(i)))
    choices_final=tuple(chap_choices)
    
    chapter_dd = forms.ChoiceField(label = "Chapter",required=False,choices=choices_final)
    right_lang_dd = forms.ChoiceField(label = "Right Language",choices=right_lang)
    left_lang_dd = forms.ChoiceField(label = "Left Language",choices = left_lang)
    search_field = forms.CharField(label = "Search Texts")
    #class Texts end



#visual_dropdown = Texts(auto_id = False)
#print visual_dropdown
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





    if request.method == "POST":
        #posted_form = Texts(request.POST)
        book = request.POST["book_dd"]
        print book
        chapter = request.POST['chapter_dd']
        from_lang = request.POST['left_lang_dd']
        to_lang = request.POST['right_lang_dd']
        path1 = "texts/"+book+"/"+from_lang.upper()+"/"+chapter+".html"
        path2 = "texts/"+book+"/"+to_lang.upper()+"/"+chapter+".html"
        print path1
    else:
        path1 = "texts/Bible_Genesis/EN/ch_1.html"
        path2 = "texts/Bible_Genesis/HE/ch_1.html"

    page1 = strip_page(parse_html(path1))
    page2 = strip_page(parse_html(path2))
    form_test = Search()

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
                    'username': username})

