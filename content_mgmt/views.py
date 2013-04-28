"""
This renders the homepage
"""
from django.shortcuts import render
import content_mgmt.scripts.parse_text_to_html 
from content_mgmt.models import UploadForm
from django.template import Context, Template 

def upload(request):
    if False:
        form = UploadForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/uploadConfirm/')
        else:
            1;
    else:

        form = UploadForm()
        return render(request, 'content_mgmt/upload.html', { 'form': form, 'title': "Upload Content"})


if __name__=='__main__':
    1
