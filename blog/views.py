from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.forms import UserCreationForm


def home(request):
    context = {
        'posts' : Posts.objects.all(),
        'title':'Home'
    }
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html',{'title':'about'})


def reg(request):
    form = UserCreationForm()
    return render(request,'reg.html',{'title':'Register','form':form})


def dod(request,id):
    return HttpResponse("<h1> fuck you " + str(id))