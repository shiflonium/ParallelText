"""
This renders the homepage
"""
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    """
    this method is responsible for drawing the homepage
    """
    username = User.objects.get(username=request.user).username
    return render(request, 'home/index.html',
                  {'include_css': 'home/home.css',
                   'include_js': 'home/slideshow.js',
                   'onload': 'playImage(\'slideImg\')',
                   'homepage': True,
                   'username': username
                  })

