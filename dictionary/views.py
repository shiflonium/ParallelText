"""
This renders the user's dictionary pages
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from languages.models import Languages
from dictionary.forms import DictLangForm
from languages.models import UserDictionary
from ptext.views import CustomDict

def viewdict(request):
    """
    This show all words the user has saved in their dictionary.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        userid = User.objects.get(username=request.user).id
        username = User.objects.get(username=request.user).username
        form = DictLangForm(request.GET)
        user_dictionary_list = UserDictionary.objects.filter(userID = userid)
        definitions_list = list()
        for i in range (0,len(user_dictionary_list)):
            definitions_list.append(user_dictionary_list[i].definitionID)



        print definitions_list

        return render(request, 'dictionary/dictionary.html',
                      {'form': form,
                       'username': username})

