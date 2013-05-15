"""
forms.py creates and defines the structure for the forms before displaying them
on the webpage. The forms determines the requirements and behavior of the input
fields presented to the user.
"""
from django import forms
from languages.models import Languages

class DictLangForm(forms.ModelForm):
    """
    DictLang provides the form model for setting dictionary language.
    """
    #def __init__(self):
        #pass

    dict_lang = forms.ModelChoiceField(
        widget = forms.Select,
        queryset = Languages.objects.all(),
    )

    class Meta:
        """
        Model metadata used to identify attributes in form data when submitting
        """
        def __init__(self):
            pass

        model = Languages
        fields = (
            'dict_lang',
        )

