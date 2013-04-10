"""
views.py decides what to display on webpage based on current conditions.
The register views checks if the user has submitted information and displays
the corresponding page after processing the information.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from register.forms import AccountCreateForm

def user_reg(request):
    """
    This is used for displaying the registration webpage
    Perhaps you need to rethink the relationship
    between this page and the models.py
    """
    form = AccountCreateForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AccountCreateForm()

    return render(request, 'register/register.html', {'form': form})

