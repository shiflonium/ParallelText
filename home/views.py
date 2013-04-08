"""
This renders the homepage
"""
from django.shortcuts import render

def index(request):
    """ 
    this method is responsible for drawing the homepage
    """
    return render(request, 'home/index.html', 
                  {'include_css': 'home.css', 'include_js':
                    'slideshow.js', 'onload': 
                    'playImage(\'slideImg\')'})

