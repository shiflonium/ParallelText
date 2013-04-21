from django.db import models

# Create your models here.

from django.shortcuts import render

def search(request):
    '''
    this is the search function which
    shows up the search page
    '''
    return render(request, 'search/search.html')