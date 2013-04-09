"""
There are the models for registering users.
There seems to be a lot of functionality in these files
should there be?  Or are these just database proxies?
"""
from django.db import models

class UserAccountCreate(models.Model):
    username = models.CharField(
        max_length = 30,
    )
    password1 = models.CharField(
        max_length = 128,
    )
    password2 = models.CharField(
        max_length = 128,
    )
    email = models.EmailField(
        max_length = 75,
        #label = 'Email Address',
        #required = False,
        #help_text = "Optional. Enter a valid email address.",
    )
    first_name = models.CharField(
        max_length = 30,
        #label = 'First Name',
        #required = False,
        #help_text = "Optional. Enter your first name.",
    )
    last_name = models.CharField(
        max_length = 30,
        #label = 'First Name',
        #required = False,
        #help_text = "Optional. Enter your last name.",
    )
    #native_lang = forms.ChoiceField(
        #label = 'Native Language',
        #choices = (
            # Language Codes
            # http://msdn.microsoft.com/en-us/library/ms533052%28v=vs.85%29.aspx
            # http://www.lingoes.net/en/translator/langcode.htm
            #('en',  'English'),
            #('he',  'Hebrew'),
            #('es',  'Spanish'),
        #)
    #)

