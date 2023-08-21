from datetime import datetime

from django.urls import reverse_lazy, reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, RequestsClient

from .models import Movies
from .serializers import MoviesSerializer

class MovieTestCase(APITestCase):
    def test_create_movie(self):
        url = reverse_lazy('movies-list')
    
        data = {
            'title': 'title Test', 
            'description': 'description Test',
            'genres': 'genres Test',
            'release_date': datetime.today().strftime('%Y-%m-%d'),
            'vote_average': '7.5',
            'vote_count': '100',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_movies(self):
        response = self.client.get(reverse('movies-list'))
        assert response.status_code == 200