# Create your views here.

from django.shortcuts import render
#from django.contrib.auth.models import User

def search(request):
    """
    this method is responsible for drawing the search page
    """
    #username = User.objects.get(username=request.user)
    return render(request, 'search/search.html',
                  {'include_css': 'home.css',
                   'include_js': 'slideshow.js',
                   'onload': 'playImage(\'slideImg\')',
                   #'username': username
                  })