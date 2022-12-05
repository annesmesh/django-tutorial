from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if request.GET.get('numbers'):
        characters.extend("0123456789")

    if request.GET.get('special'):
        characters.extend("!@#$%^&*()")

    length = int(request.GET.get('length', 8))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def description(request):
    return render(request, 'generator/description.html')
