"""
views.py decides what to display on webpage based on current conditions.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import AccountCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_reg(request):
    """
    The register views checks if the user has submitted information and displays
    the corresponding page after processing the information.
    """
    form = AccountCreateForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AccountCreateForm()

    return render(request, 'users/register.html', {'form': form})



def user_auth(request):
    """
    This function authenticates a user on her login,
    either approving or rejecting the login/password
    """
    status = ""
    username = password = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                status = "You have successfully logged in!"
            else:
                status = "You have logged in but your account is inactive.\
                  Please contact an administrator."
        else:
            status = "Your username and/or password were incorrect."

    return render(request, 'users/login.html',
                  {'status': status, 'username': username})



def user_logout(request):
    logout(request)
    response = redirect('home.views.index')
    response.delete_cookie('user_location')
    return response



def user_acct(request):
    return render(request, 'users/account.html')

