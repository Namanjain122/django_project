# newscraper/urls.py

from django.urls import path
from .views import scrape_crypto
urlpatterns = [
    
    path('', scrape_crypto, name='scrape_crypto'),
]
