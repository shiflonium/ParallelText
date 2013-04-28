"""
This renders the homepage
"""
from django.shortcuts import render
import content_mgmt.scripts.parse_text_to_html 
from content_mgmt.models import UploadForm
from django.template import Context, Template 
from django.http import HttpResponseRedirect

def upload_fail(request):
    return render(request, 'content_mgmt/upload_fail.html')

def upload_confirm(request):
    return render(request, 'content_mgmt/upload_confirm.html')

def upload(request):
    if request.method=="POST":
        form = UploadForm(request.POST)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['file'])
            return HttpResponseRedirect('/upload_confirm/')
        else:
            return HttpResponseRedirect('/upload_fail/', {'form':form, 'dog' : "shorty" })
    else:
        form = UploadForm()
        return render(request, 'content_mgmt/upload.html', { 'form': form, 'title': "Upload Content"})


if __name__=='__main__':
    1
