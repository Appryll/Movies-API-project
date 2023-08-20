import django_filters
from .models import Movies

class MoviesFilter(django_filters.FilterSet):
    genres = django_filters.CharFilter(field_name='genres', lookup_expr='icontains')

    release_date_gte = django_filters.DateFilter(field_name='release_date', lookup_expr= 'gte', label='before')
    release_date_lte = django_filters.DateFilter(field_name='release_date', lookup_expr='lte', label='after')
    class Meta:
        model = Movies
        fields = {
            'vote_average' : ['range',]
        }