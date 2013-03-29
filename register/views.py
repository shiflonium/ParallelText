from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import UserCreationForm

def user_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'register/register.html', {'form': form})

