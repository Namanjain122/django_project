# newscraper/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import scrape_crypto_data
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

@api_view(['POST'])
def scrape_crypto(request):
    if request.method == 'POST':
        coins = request.data.get('coins', [])
        
        # Trigger the Celery task
        task = scrape_crypto_data.delay(coins)
        
        # Return a response
        return Response({'task_id': task.id}, status=202)
