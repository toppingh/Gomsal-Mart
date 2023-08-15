from django.urls import path
from .views import searchResult

app_name = 'search'

urlpatterns = [
    path('search/', searchResult, name='searchResult'),
]