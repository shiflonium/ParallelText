"""
This displays the web registration webpage
"""

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import UserCreationForm

def user_reg(request):
    """
    This is used for displaying the registration webpage
    Perhaps you need to rethink the relationship
    between this page and the models.py
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'register/register.html', {'form': form})

