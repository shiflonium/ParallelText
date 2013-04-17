"""
views.py decides what to display on webpage based on current conditions.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import AccountCreateForm, AccountManageForm
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
    This function authenticates a user on login, either approving or rejecting
    the provided credentials.
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
    """
    This function deauthenticates the current user from the system.
    """
    logout(request)
    response = redirect('home.views.index')
    response.delete_cookie('user_location')
    return response



def user_acct(request):
    """
    This function allows the current user to view their account information
    and perform any changes to them, if necessary.
    """
    form = AccountManageForm()
    username = User.objects.get(pk=1)
    form = AccountManageForm(instance=username)
    return render(request, 'users/account.html',
                  {'form': form,
                   'username': username})



def del_acct(request):
    """
    This function allows the current user to delete their account from the
    system.
    """
    username = User.objects.get(username=request.user)
    username.delete()
    return HttpResponseRedirect('/')

