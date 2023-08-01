from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('signup/', views.signUp, name='signup'),
    path('logout/', views.logout, name='logout'),
]