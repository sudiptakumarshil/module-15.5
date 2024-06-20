from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from .models import Album

# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'Your form has been submitted successfully!')
            return redirect('album.add')
    form = forms.AlbumForm()
    return render(request,'add_album.html',{'form':form})


def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'The album has been updated successfully!')
            return redirect('home')
        
    return render(request,'add_album.html',{'form':album_form})

def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('home')