"""
forms.py creates and defines the structure for the forms before displaying them
on the webpage. The forms determines the requirements and behavior of the input
fields presented to the user.
"""
from django import forms

class Texts(forms.Form):
    chapter_dd = forms.ChoiceField(label = "Chapter")
    right_lang_dd = forms.ChoiceField(label = "Right Language")
    left_lang_dd = forms.ChoiceField(label = "Left Language")

class Book(forms.Form):
    book_dd = forms.ChoiceField(label = "Select Book")