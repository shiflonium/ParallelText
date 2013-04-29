#from django.db import models
"""
This file would contain the models for the home funcion
but currently no models are being used
"""

from django import forms
from languages.models import Languages
# Create your models here.

class UploadForm (forms.Form):
#    import pdb; pdb.set_trace()
    choices = Languages.objects.all().values_list('abbr', 'name')
    language=forms.ChoiceField(choices)
    title=forms.CharField(label="Book Title: ")
    file=forms.FileField(label="Upload File: ")
