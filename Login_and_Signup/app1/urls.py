from django.contrib import admin
from django.urls import path, include
from . import views
from home.views import signup_view, login_view, about, home_view

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
