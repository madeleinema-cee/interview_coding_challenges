from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Company Headcount'),
    path('about/', views.about, name='about'),
]