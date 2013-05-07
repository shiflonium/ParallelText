"""
This renders the user's dictionary pages
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from languages.models import Languages
from dictionary.forms import DictLangForm

def viewdict(request):
    """
    This show all words the user has saved in their dictionary.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        username = User.objects.get(username=request.user).username
        form = DictLangForm(request.GET)
        return render(request, 'dictionary/dictionary.html',
                      {'form': form,
                       'username': username})

