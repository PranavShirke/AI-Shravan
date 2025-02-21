from django.contrib import admin
from django.urls import include, path
from Bindaas.views import gestures, home, landing
from Bindaas import views

urlpatterns = [ 
    path('', views.landing, name='landing'),
    path('gestures/', views.gestures, name='gestures'),
    path('home/', views.home, name='home'),
]