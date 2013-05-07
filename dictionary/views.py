"""
This renders the user's dictionary pages
"""

from django.shortcuts import render
from django.contrib.auth.models import User

def viewdict(request):
    """
    This show all words the user has saved in their dictionary.
    """
    if request.user.is_authenticated():
        username = User.objects.get(username=request.user).username
    else:
        username = ''

    return render(request, 'dictionary/dictionary.html', {'username': username})


