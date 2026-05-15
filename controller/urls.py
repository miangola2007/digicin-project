# Fichier : controller/urls.py
from django.urls import path
from . import views

app_name = 'controller'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('examine/<uuid:pk>/', views.examine, name='examine'),
]