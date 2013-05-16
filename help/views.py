"""
This renders the help page
"""
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    """
    this method is responsible for drawing the help page
    """
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user).username
    else:
        username = ''

    return render(request, 'help/help.html', {'username': username})

