from rest_framework import serializers

from .models import Movies
class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'
        read_only_fields = ('release_date',)