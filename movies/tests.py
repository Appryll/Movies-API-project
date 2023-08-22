from datetime import datetime

from django.urls import reverse_lazy, reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Movies

class MoviesTestCase(APITestCase):
    data = {
        'title': 'title Test', 
        'description': 'description Test',
        'genres': 'genres Test',
        'release_date': datetime.today().strftime('%Y-%m-%d'),
        'vote_average': '7.5',
        'vote_count': '100',
    }

    update_data = {
        'title': 'title Test-update', 
        'description': 'description Test-update',
        'genres': 'genres Test-update',
        'release_date': datetime.today().strftime('%Y-%m-%d'),
        'vote_average': '7.5',
        'vote_count': '100',
    }

    # Test créer un nouveau film
    def test_create_new_movie(self):   
        res = self.client.post(reverse_lazy('movies-list'), self.data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movies.objects.count(), 1)
        self.assertEqual(Movies.objects.get().title, 'title Test')

    # Test return list des films avec status_code 200
    def test_list_movies(self):
        response = self.client.get(reverse('movies-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #assert response.status_code == 200

    # Test return detail du film avec status_code 200 et 404 not found
    def test_detail_movie(self):
        # détails id correct
        res = self.client.post(reverse_lazy('movies-list'), self.data, format='json')
        response = self.client.get(reverse_lazy('movies-detail', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'title Test')
        # détails id incorrect
        response_not_found = self.client.get(reverse_lazy('movies-detail', kwargs={"pk": 3}))
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)

    # Test mise à jour du film
    def test_update_movie(self):
        res = self.client.post(reverse_lazy('movies-list'), self.data, format='json')
        response = self.client.put(reverse_lazy('movies-detail', kwargs={"pk": 1}), self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test suppresion du film
    def test_delete_movie(self):
        res = self.client.post(reverse_lazy('movies-list'), self.data, format='json')
        response = self.client.delete(reverse_lazy('movies-detail', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movies.objects.count(), 0)