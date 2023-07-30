from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='shop/login_page.html'), name='login'),
    #path('login/signup/', views.signup, name='signup'), # login/signup/으로 하신 이유가 있을까욥??
]