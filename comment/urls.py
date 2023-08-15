from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('create/<int:product_id>/', views.create_comment, name='create'),
]