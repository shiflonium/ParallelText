#from django.db import models
"""
This file would contain the models for the home funcion
but currently no models are being used
"""

from django import forms
from languages.models import Languages
# Create your models here.

class UploadForm (forms.Form):
    language=forms.ModelMultipleChoiceField(widget=forms.Select,
        queryset=Languages.objects.all().values_list('name', flat=True))
    title=forms.CharField(label="Book Title: ")
    file=forms.FileField(label="Upload File: ")
