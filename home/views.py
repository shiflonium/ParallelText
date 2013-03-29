from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {'include_js': 'slideshow.js', 'onload': 'switchImage(\'slideImg\')'})

