"""
This renders the homepage
"""
from django.shortcuts import render
from content_mgmt.scripts.parse_text_to_html import convert_book_to_html
from content_mgmt.forms import UploadForm
from django.template import Context, Template 
from django.http import HttpResponseRedirect
import re


def upload_fail(request):
    return render(request, 'content_mgmt/upload_fail.html')

def upload_confirm(request):
    return render(request, 'content_mgmt/upload_confirm.html')

def upload(request):
    if request.method=="POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc =  request.FILES['file']
            lang = request.POST['language']
            title = request.POST['title']
            bookdir = re.sub("\s+", "_", title)
            convert_book_to_html(bookdir, lang, title,  newdoc.read())
            return HttpResponseRedirect('/upload_confirm/')
    else:
        form = UploadForm()
    return render(request, 'content_mgmt/upload.html', { 'form': form, 'title': "Upload Content"})


if __name__=='__main__':
    1
