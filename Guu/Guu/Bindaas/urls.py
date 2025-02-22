from django.urls import path
from Bindaas import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('speech_to_text/', views.speech_to_text, name='speech_to_text'),
    path('gesture_recognition/', views.gesture_recognition, name='gesture_recognition'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('video_tutorials/', views.video_tutorials, name='video_tutorials'),
    path('gestures/', views.gestures, name='gestures'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
    path('api/transcribe/', views.transcribe_audio, name='transcribe_audio'),

    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),
]

