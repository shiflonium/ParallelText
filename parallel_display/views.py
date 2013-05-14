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
from books.models import BookInfo, BookTranslation
from languages.models import Languages
from parallel_display.forms import Book, Texts
from django.shortcuts import render 
from django.core.context_processors import csrf
from bs4 import BeautifulSoup
from ptext.views import strip_page
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
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

def det_text_dir(language):
    """
    this function is a helper function to determine 
    text direction depending on the selected language 
    in the parallel display
    """
    right_dir_lang = ['he','ar']
    if language.lower() in right_dir_lang:
        return 'right'
    else:
        return 'left'


def parse_html(filepath):
    """parse_html takes an html file path and strips
    all tags from it besides <p> tags. the <p> tags are added
    to a list. parse_html returns a joined list as a string"""
    page = str(get_page(filepath))
    p_tag_list = re.findall('<p.*?</p>' , page , re.DOTALL)
    p_tag_string = "" . join(p_tag_list)
    return p_tag_string

def selectLang(book_from_form, form):
    
    """
    This function is a helper function to populate our language and chapters form
    it makes a call to our database using saved information from the first form
    """

    lang_choices = []
    chap_choices = []
    chap_num = BookInfo.objects.filter(title = book_from_form)
    all_translations = BookTranslation.objects.filter(
        book_id = int(chap_num[0].id))
    for i in range(0, int(chap_num[0].chaps)):
        chap_choices.append(("ch_" + str(i + 1), "Chapter " + str(i + 1)))
    for tran in all_translations:
        lang = tran.language_id
        lang_name = lang.name
        lang_abbr = lang.abbr
        lang_choices.append((lang_abbr, lang_name))
    form.fields['chapter_dd'].choices = tuple(chap_choices)
    form.fields['right_lang_dd'].choices = tuple(lang_choices)
    form.fields['left_lang_dd'].choices = tuple(lang_choices)
    
def get_lang_name(book_name): #for future generation of language headers

    """
    this function is a helper function to create a lang_dictionary
    of languages and their language codes. we are going to use this function
    for generating headers for our parallel display
    this function returns a dictionary
    """
    lang_choices = []
    id_of_book = BookInfo.objects.filter(title = book_name)
    all_translations = BookTranslation.objects.filter(
        book_id = int(id_of_book[0].id))
    for tran in all_translations:
        lang = tran.language_id
        lang_name = lang.name
        lang_abbr = lang.abbr
        lang_choices.append((lang_abbr, lang_name))
    lang_tuple = tuple(lang_choices)
    lang_dictionary = dict((x, y) for x, y in lang_tuple)
    return lang_dictionary

def get_chap_name(book_name):

    """
    this function is a helper function to create a dictionary
    of chapters and their chapter values from dropdown. we are going to use this function
    for generating headers for our parallel display
    this function returns a dictionary
    """

    chap_choices = []
    chap_num = BookInfo.objects.filter(title = book_name)
    all_translations = BookTranslation.objects.filter(
        book_id = int(chap_num[0].id))
    for i in range(0, int(chap_num[0].chaps)):
        chap_choices.append(("ch_" + str(i + 1), "Chapter " + str(i + 1)))
    chap_tuple = tuple(chap_choices)
    chap_dictionary = dict((x, y) for x, y in chap_tuple)
    return chap_dictionary



def select_book(request):

    """
    This function takes the two texts, parses them both,
    and inserts them into the right and left windows.

    this function is built from 2 forms dependent on each other.
    it populates the forms from the database

    Importantly, we must pass along information here about
    whether the text flows Right To Left or Left To Right
    """

    book_list = []
    selected_book = ""
    book_form = Book()
    lang_form = Texts()
    all_books = BookInfo.objects.all()
    for book in all_books:
        title = book.title
        title_regex = re.sub("_", " ", title)
        book_list.append((title, title_regex))
    selects = tuple(book_list)
    book_form.fields['book_dd'].choices = selects
    if request.method == "POST":
        if "book_submit" in request.POST:
            selected_book = request.POST['book_dd']
            request.session['saved_book_name'] = selected_book
            selectLang(selected_book, lang_form)
            book_title = re.sub("_", " ", selected_book)
            return render(request, 'parallel_display/select_lang.html',
            {'form':lang_form, 'book_header':book_title})
        if "chap_lang_submit" in request.POST:
            final_book = request.session.get('saved_book_name')
            final_chapter = request.POST['chapter_dd']
            right = request.POST['right_lang_dd']
            left = request.POST['left_lang_dd']
            path_right = "texts/%s/%s/%s.html" % (final_book,
            right.upper(), final_chapter)
            path_left = "texts/%s/%s/%s.html" % (final_book,
                left.upper(), final_chapter)
            right_page = strip_page(parse_html(path_right))
            left_page = strip_page(parse_html(path_left))
            lang_dict = get_lang_name(final_book) 
            chap_dict = get_chap_name(final_book)
            chosen_book = re.sub("_", " ", final_book)
            chosen_chapter = chap_dict[final_chapter]
            right_lang_header = lang_dict[right]
            left_lang_header = lang_dict[left]

            text1_dir = det_text_dir(left)
            text2_dir = det_text_dir(right)

            print text1_dir
            print text2_dir

            if request.user.is_authenticated():
                username = User.objects.get(username=request.user).username
            else:
                username = ''
            return render (request,
            "ptext/popupDemo.html",
            {'myTitle':'Demo', 'css_url':'parallel_display/popup.css',
            'chosen_chapter':chosen_chapter, 'text1':left_page, 'text2':right_page,
            'img_url':'parallel_display/Info.png','chosen_book':chosen_book,
            'text1Dir':text1_dir, 'text2Dir':text2_dir, 'left_lang':left_lang_header,
            'username': username, 'right_lang':right_lang_header})
    return render(request,
                   "parallel_display/select_book.html", {'form':book_form})



