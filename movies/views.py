from django.db.models import Q
from django.shortcuts import redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import MoviesFilter
from .models import Movies
from .serializers import MoviesSerializer

# Pagination
class MovieSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MoviesViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given movie.

    list:
        Return a list of all movies.

    create:
        Create a new movie.

    destroy:
        Delete a movie.

    update:
        Update a movie.

    partial_update:
        Update a movie.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = MoviesSerializer
    pagination_class = MovieSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MoviesFilter
    
    def get_queryset(self):
        return Movies.objects.all()

class MovieListTitleDescriptionFilter(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()

    # only the GET method will be shown in Swagger
    @swagger_auto_schema(operation_description="partial_update description override", responses={200: MoviesSerializer, 404: 'slug not found'})
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params)
        movies = Movies.objects.filter( Q(title__icontains=params['pk']) | Q(description__icontains=params['pk']))
        serializers= MoviesSerializer(movies, many=True)
        return Response(serializers.data)