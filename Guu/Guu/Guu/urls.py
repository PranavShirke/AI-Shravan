from django.contrib import admin
from django.urls import include, path
from Bindaas.views import gestures, home, landing, speech_to_text, text_to_speech, gesture_recognition, chatbot, video_tutorials
from Bindaas import views

urlpatterns = [ 
    path('', views.landing, name='landing'),
    path('gestures/', views.gestures, name='gestures'),
    path('home/', views.home, name='home'),
    path('speech_to_text/', views.speech_to_text, name='speech_to_text'),
    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),
    path('gesture_recognition/', views.gesture_recognition, name='gesture_recognition'),
    path('chatbot/', views.chatbot, name ='chatbot'),
    path('video_tutorials/', views.video_tutorials, name='video_tutorials'),
]