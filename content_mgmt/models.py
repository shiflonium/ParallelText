#from django.db import models
"""
This file would contain the models for the home funcion
but currently no models are being used
"""

from django import forms
# Create your models here.

class UploadForm (forms.Form):
    language=forms.ChoiceField 
    (
        ('EN', 'English'),
        ('AR', 'Arabic'),
        ('ZH', 'Chinese'),
        ('FR', 'French'),
        ('EL', 'Greek'),
        ('HE', 'Hebrew'),
        ('KO', 'Korean'),
        ('LA', 'Latin'),
        ('PT', 'Portuguese'),
        ('RU', 'Russian'),
        ('ES', 'Spanish'),
        ('TH', 'Thai'),
        ('UK', 'Ukranian'),
        
        )
    title=forms.CharField()
    file=forms.FileField()
