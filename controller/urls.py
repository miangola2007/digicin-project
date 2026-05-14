from django.urls import path
from . import views

app_name = 'controller'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('examiner/<uuid:pk>/', views.examine_cin, name='examine'),
    path('valider/<uuid:pk>/', views.action_validate, name='action_validate'),
]