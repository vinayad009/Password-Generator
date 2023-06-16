from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?'))

    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request, 'password.html', {'password': thepassword})

def about(request):
    return render(request, 'about.html')