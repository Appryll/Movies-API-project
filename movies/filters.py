import django_filters
from .models import Movies
from django.db.models import Q

class MoviesFilter(django_filters.FilterSet):
    genres = django_filters.CharFilter(field_name='genres', lookup_expr='icontains')

    before = django_filters.DateFilter(field_name='release_date', lookup_expr= 'gte', label='before')
    after = django_filters.DateFilter(field_name='release_date', lookup_expr='lte', label='after')
    class Meta:
        model = Movies
        fields = {
            'vote_average' : ['range',]
        }