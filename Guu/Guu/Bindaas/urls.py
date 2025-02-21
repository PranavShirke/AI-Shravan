from django.urls import path
from Bindaas import views 


urlpatterns = [
    path('Bindaas/', views.bindaas_view, name='Bindaas'),
]

