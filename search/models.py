from django.db import models

# Create your models here.

from django.shortcuts import render

def search(request):
    return render(request, 'search/search.html')