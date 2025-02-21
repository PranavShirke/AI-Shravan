from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, "landing.html")

def gestures(request):
    return render(request, "Gestures.html")

def home(request):
    return render(request, "home.html")
