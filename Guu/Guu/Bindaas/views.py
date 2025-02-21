from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def landing(request):
    return render(request, "landing.html")

def gestures(request):
    return render(request, "gestures.html")

def home(request):
    return render(request, "home.html")

def speech_to_text(request):
    return render(request, "speech_to_text.html")

def gesture_recognition(request):
    return render(request, "gesture_recognition.html")

def chatbot(request):
    return render(request, "chatbot.html")

def video_tutorials(request):
    return render(request, "video_tutorials.html")

def text_to_speech(request):
    return render(request, "text_to_speech.html")
