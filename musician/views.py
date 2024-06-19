from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from .models import Musician

def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        
        if musician_form.is_valid():
            musician_form.save()
            messages.success(request, 'Your form has been submitted successfully!')
            return redirect('musician.add')
        
    form = forms.MusicianForm
    data = Musician.objects.all()
    return render(request,'add_musician.html',{'form':form,'data':data})

def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            messages.success(request, 'The musician has been updated successfully!')
            return redirect('musician.add')
        
    data = Musician.objects.all()
    return render(request,'add_musician.html',{'form':musician_form,'data':data})

def delete_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('musician.add')
    