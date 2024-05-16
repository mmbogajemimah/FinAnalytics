from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path("home/", views.home, name='home_page'),
    path("register/", views.register_user, name='registration_page')
]
