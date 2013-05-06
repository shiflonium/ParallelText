# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User

def search(request):
    username = User.objects.get(username=request.user).username
    return render(request, 'search/search.html', {'username': username})

