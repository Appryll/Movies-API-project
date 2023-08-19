import pandas as pd
import sqlite3
import ast
import os  

# Générer Dataframe
df = pd.read_csv('data/movies_metadata.csv', nrows=1000)[["id", "title", "overview", "release_date", "vote_average", "vote_count"]]

# Renommer la colonne 'overview' selon cahier
df.rename(columns = {'overview':'description'}, inplace = True)

# Colonne genres --> dataframe genre
df_genre = pd.read_csv('data/movies_metadata.csv', nrows=1000)[["genres"]]

#str --> dictionnaire (genre:{0:{}})
df_dict = df_genre.to_dict()

# liste de dictionnaire de tous les films
granlist = []

for row in df_dict['genres']:
    granlist.append(ast.literal_eval(df_dict['genres'][row]))

# parcourir chaque ligne de liste et faire un liste (list_genre_movie) avec le valeur de la clé 'name' du dictionnaire
list_line = []
for linea in granlist:
    #print(linea)
    list_genre_movie = []
    for item in linea:
        genre = item['name']
        list_genre_movie.append(genre)
    #print(listgenremovie)
    list_line.append(list_genre_movie)

# #print(listadelineas)
# print(type(listadelineas))
# print(str(listadelineas))

# Concatenation des colonnes de ma liste de genres afin de gerer mon dataframe genres
my_df_genre = pd.DataFrame((zip(list_line)), columns=['genres'])
# #print(my_df_genre)

# Concatenation des dataframes afin de générer un dataframe final avec toute l'information
df_final = pd.concat([df, my_df_genre], axis=1)

# Creér dossier data s'il n'existe pas
os.makedirs('data', exist_ok=True)

# dataframe --> csv
df_final.to_csv('data/movies_data.csv')  

movies_data = pd.read_csv('data/movies_data.csv', nrows=1000)[["id", "title", "description", "genres", "release_date", "vote_average", "vote_count"]]

table_name = 'movies_movies'

# Connexion bdd
conn = sqlite3.connect('db.sqlite3')
# Creér table s'il n'existe pas
query = f'Create table if not Exists {table_name} (title text, description text, genres text, release_date text, vote_average real, vote_count integer)'
# Execution query
conn.execute(query)
# csv --> sql
movies_data.to_sql(table_name,conn,if_exists='replace',index=False)
# commit et fermeture bdd
conn.commit()
conn.close()
#print('fin')