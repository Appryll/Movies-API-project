import django_filters
from .models import Movies
from django.db.models import Q

class MoviesFilter(django_filters.FilterSet):
    movie_filter = django_filters.CharFilter(method='filter_movie')

    """Filter for Books by Price"""
    vote_average = django_filters.RangeFilter()

    class Meta:
        model = Movies
        fields = ['vote_average', ]
        # fields = {
        #     'genres': ['icontains'],
        #     'vote_average' : ['lte', 'gte'],
        #     'before' : movie_filter

        # }
        #fields = ['genre', 'release_date__lte', 'movie_filter']
        
    # def filter_movie(self, qs, name, value):
    #     return qs.filter(
    #         Q(client_id__last_name__icontains=value) | Q(client_id__email__icontains=value)
    #     )

# qs = Movies.objects.all()

# # Range: vote_average between 0 and 10
# f = F({'vote_average_min': '0', 'vote_average_max': '10'}, queryset=qs)