"""
This renders the homepage
"""
from django.shortcuts import render
import content_mgmt.scripts.parse_text_to_html 
from content_mgmt.models import UploadForm

def index(request):
    """ 
    this method is responsible for drawing the homepage
    """
    return render(request, '/upload.html')



def upload(request):
    if False:
        form = UploadForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/uploadConfirm/')
        else:
            1;
    else:
        print "moo"
        form = UploadForm()
    return render(request, 'content_mgmt/upload.html', { 'form': form, })


if __name__=='__main__':
    1
