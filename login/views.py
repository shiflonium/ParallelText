"""
This file implements the login feature 
"""
from django.contrib.auth import authenticate, login
from django.shortcuts import render

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

    return render(request, 'login/login.html', 
                  {'status': status, 'username': username})

