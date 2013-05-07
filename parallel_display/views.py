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


left_lang_g = (
        ("en","English"),("la","Latin"),
        ("he","Hebrew"),("ko","Korean"),
        ("el","Greek"),("uk","Ukrainian"),
        ("es","Spanish"),("th","Thai"),
        ("pt","Portuguese"),
        ("ru","Russian"),
        ("ar","Arabic"),
        )

right_lang_g = (
        ("en","English"),("la","Latin"),
        ("he","Hebrew"),("ko","Korean"),
        ("el","Greek"),("uk","Ukrainian"),
        ("es","Spanish"),("th","Thai"),
        ("pt","Portuguese"),
        ("ru","Russian"),
        ("ar","Arabic"),
        )

left_lang_q = (
        ("en","English"),("bs","Bosnian"),
        ("he","Hebrew"),("de","German"),
        ("el","Greek"),("fr","French"),("ms","Malay"),
        ("es","Spanish"),("hr","Hungarian"),("pl","Polish"),
        ("id","Indonisian"),("sw","Swahili"),("tr","Turkish"),
        ("ru","Russian"),("it","Italian"),("zh","Chinese"),
        ("ar","Arabic"),("ja","Japanese"),
        )

right_lang_q = (
        ("en","English"),("bs","Bosnian"),
        ("he","Hebrew"),("de","German"),
        ("el","Greek"),("fr","French"),("ms","Malay"),
        ("es","Spanish"),("hr","Hungarian"),("pl","Polish"),
        ("id","Indonisian"),("sw","Swahili"),("tr","Turkish"),
        ("ru","Russian"),("it","Italian"),("zh","Chinese"),
        ("ar","Arabic"),("ja","Japanese"),
        )




class Texts(forms.Form):
    b=BookInfo.objects.filter(title="Quran")
    chap_num_str=b[0].chaps
    chap_num=int(chap_num_str)
    chap_choices=[]
    for i in range (0,chap_num+1):
        chap_choices.append(("ch_"+str(i+1),"Chapter "+str(i+1)))
    choices_final=tuple(chap_choices)
    book_dd_q = "Quran"
    chapter_dd_q = forms.ChoiceField(label = "Chapter",required=False,choices=choices_final)
    right_lang_dd_q = forms.ChoiceField(label = "Right Language",choices=right_lang_q)
    left_lang_dd_q = forms.ChoiceField(label = "Left Language",choices = left_lang_q)
    #search_field_q = forms.CharField(label = "Search Texts")
    #class Texts end
    g=BookInfo.objects.filter(title="Bible_Genesis")
    chap_num_str_g=g[0].chaps
    chap_num_g=int(chap_num_str_g)
    chap_choices_g=[]
    for k in range (0,chap_num_g):
        chap_choices_g.append(("ch_"+str(k+1),"Chapter "+str(k+1)))
    choices_final_g=tuple(chap_choices_g)
    book_dd_g = "Genesis"
    chapter_dd_g = forms.ChoiceField(label = "Chapter",required=False,choices=choices_final_g)
    right_lang_dd_g = forms.ChoiceField(label = "Right Language",choices=right_lang_g)
    left_lang_dd_g = forms.ChoiceField(label = "Left Language",choices = left_lang_g)



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
    right_header=''
    left_header=''



    form=Texts(request.POST)
    if request.method == "POST" and form.is_valid():       
        if "quran_submit" in request.POST:
            
        #posted_form = Texts(request.POST)
        #book = request.POST["book_dd"]
            book="Quran"
            chapter = request.POST['chapter_dd_q']
            from_lang = request.POST['left_lang_dd_q']
            to_lang = request.POST['right_lang_dd_q']
            path1 = "texts/"+book+"/"+from_lang.upper()+"/"+chapter+".html"
            path2 = "texts/"+book+"/"+to_lang.upper()+"/"+chapter+".html"
        if "genesis_submit" in request.POST:
            book="Bible_Genesis"
            chapter = request.POST['chapter_dd_g']
            from_lang = request.POST['left_lang_dd_g']
            to_lang = request.POST['right_lang_dd_g']
            path1 = "texts/"+book+"/"+from_lang.upper()+"/"+chapter+".html"
            path2 = "texts/"+book+"/"+to_lang.upper()+"/"+chapter+".html"
            
    else:
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

