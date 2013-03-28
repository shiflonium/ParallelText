from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import UserCreationForm

def user_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

