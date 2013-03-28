#from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    native_language = forms.ChoiceField(choices=(
        # Language Codes
        # http://msdn.microsoft.com/en-us/library/ms533052%28v=vs.85%29.aspx
        # http://www.lingoes.net/en/translator/langcode.htm
        ('en',  'English'),
        ('he',  'Hebrew'),
        ('es',  'Spanish'),
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'native_language'
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user

