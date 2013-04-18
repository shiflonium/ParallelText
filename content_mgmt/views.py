"""
This renders the homepage
"""
from django.shortcuts import render
import .parsing_scripts.parse_text_to_html 


def index(request):
    """ 
    this method is responsible for drawing the homepage
    """
    return render(request, '/upload.html')



def upload(request):
    if request.method=='POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/uploadConfirm/')
        else:
            1;
    else:
        form = UploadForm()
    return render(request, 'upload.html', { 'form': form, })
