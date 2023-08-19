from rest_framework import serializers
from .models import Movies
import ast

import pandas as pd

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'
        read_only_fields = ('release_date',)
    
    # def to_representation(self, instance):

    #     ret = super(MoviesSerializer, self).to_representation(instance)
    #     ret['genres'] = Movies.objects.values()
    #     return ret

    #     df_dict = df_genre.to_dict()

    #     granlist = []

    #     for row in df_dict['genres']:
    #         granlist.append(ast.literal_eval(df_dict['genres'][row]))

    #     #print(granlist[0])

    #     listadelineas = []
    #     for linea in granlist:
    #         #print(linea)
    #         listgenremovie = []
    #         for item in linea:
    #             genre = item['name']
    #             listgenremovie.append(genre)
    #         #print(listgenremovie)
    #         listadelineas.append(listgenremovie)


    #     # str a list
    #     # dict_genre = ast.literal_eval(ret['genres']) 
    #     # print(type(dict_genre))
    #     # mylist = []
    #     # for row in dict_genre:
    #     #     genre = row['name']
    #     #     mylist.append(genre)
    #     print(type(ast.literal_eval(ret['genres'])))
    #     #ret['genres'] = ast.literal_eval(ret['genres'])[0]['name']
    #     ret['genres'] = ['name', 'name']
    #     return ret