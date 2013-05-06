# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User

def search(request):
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user).username
    else:
        username = ''

    username = User.objects.get(username=request.user).username
    return render(request, 'search/search.html', {'username': username})

