from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'applausable/home.html')

def artist(request):
    return render(request, 'applausable/artist.html')

def signUp(request):
    return render(request, 'applausable/SignUp.html')