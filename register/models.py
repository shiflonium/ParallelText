#from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label = 'Email Address',
        required = False,
        help_text = "Optional. Enter a valid email address.",
    )
    first_name = forms.CharField(
        #label = 'First Name',
        required = False,
        help_text = "Optional. Enter your first name.",
    )
    last_name = forms.CharField(
        #label = 'First Name',
        required = False,
        help_text = "Optional. Enter your last name.",
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

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            #'native_lang'
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.native_lang = native_lang

        if commit:
            user.save()

        return user

