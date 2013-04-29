"""
views.py decides what to display on webpage based on current conditions.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import AccountCreateForm, AccountManageForm
from users.forms import AccountManagePassForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import UserAccount
from languages.models import Languages

def user_reg(request):
    """
    The register views checks if the user has submitted information and displays
    the corresponding page after processing the information.
    """
    form = AccountCreateForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password1'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'))
            lang = Languages.objects.get(langID=request.POST.get('native_lang'))
            extra_info = UserAccount(user_id=new_user.pk, native_lang=lang)
            extra_info.save()
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
    status = ""

    user = User.objects.get(username=request.user.username)
    lang_id = UserAccount.objects.get(user_id=request.user.pk).native_lang_id
    lang_name = Languages.objects.get(langID=lang_id)

    if request.method == 'POST':
        form = AccountManageForm(data=request.POST, instance=request.user)
        if form.is_valid():
            extra_info = UserAccount.objects.get(user_id=user.pk)
            extra_info.native_lang_id = request.POST.get('native_lang')
            extra_info.save()
            form.save()
            status = "Your account information has been saved."
    else:
        form = AccountManageForm(instance=request.user,
                                 initial={'native_lang': lang_name})

    return render(request, 'users/account.html',
                  {'form': form,
                   'status': status,
                   'username': user.username})



def user_acct_pass(request):
    """
    This function allows the current user to view their account information
    and perform any changes to them, if necessary.
    """
    status = ""

    username = User.objects.get(username=request.user)

    form = AccountManagePassForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username.set_password(request.POST.get('pass_new1'))
            username.save()
            status = "Your account information has been saved."
    else:
        form = AccountManagePassForm()

    return render(request, 'users/account_pass.html',
                  {'form': form,
                   'status': status,
                   'username': username})



def del_acct(request):
    """
    This function allows the current user to delete their account from the
    system.
    """
    username = User.objects.get(username=request.user)
    username.delete()
    return HttpResponseRedirect('/')


