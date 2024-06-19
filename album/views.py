from django.shortcuts import render
from . import forms
# Create your views here.
def add_album(request):
    form = forms.AlbumForm()
    return render(request,'add_album.html',{'form':form})