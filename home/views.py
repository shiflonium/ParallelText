from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {'include_css': 'home.css', 'include_js': 'slideshow.js', 'onload': 'playImage(\'slideImg\')'})

