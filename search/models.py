from django.db import models
from django.shortcuts import render

# Create your models here.

def search(request):
    '''
    this is the search function which
    shows up the search page
    '''
    return render(request, 'search/search.html')