from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext

def user_auth(request):
    status = "Please login:"
    username = password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                status = "You have successfully logged in!"
            else:
                status = "You have logged in but your account is inactive. Please contact an administrator."
        else:
            status = "Your username and/or password were incorrect."

    return render_to_response('login.html', {'status': status, 'username': username}, context_instance=RequestContext(request))

