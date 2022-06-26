import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# credenciales
client_id = 'd79be57878574024979e595db7c3a1e2'        
client_secret = '8d91bfa471c1452fbb5c3d8afbe3283d'       

# nos conectamos a la api
client_credentials_manager = SpotifyClientCredentials( client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, language="es")

# buscamos palabras claves
words = ["leyenda", "creativo", "datos", "comedia", "cultura", "idioma", "musica", "mente", "escuelas", 
         "libros", "noticias", "deportes", "tecnología", "comida", "tacos", "educacion", "politica", 
         "negocios", "autoayuda", "historia", "finanzas", "arte", "entretenimiento", "terror", "novelas", 
         "juegos", "ajedrez", "salud", "nutricion", "futbol", "vida", "idiomas"]

for pal in words:
    # inicializamos las lista a ocupar
    id_list = []
    name = []
    fecha = []
    episodios = []
    languages = []
    for i in range(0,1000,50): # buscamos 1000 podcats de cada tema
        track_results = sp.search(q=pal, type='show', limit=50, offset=i, market="MX")
        for i, t in enumerate(track_results['shows']['items']):
            # agregamos la informacion importate de los podcasts.
            id_list.append(t["id"])
            name.append(t["name"])
            fecha.append(t["publisher"])
            episodios.append(t["total_episodes"])
            languages.append(t["languages"])

    # creamos el dataframe con los datos.
    podcast_palabra = pd.DataFrame({'name':name,'id_list':id_list,'fecha':fecha,'episodios':episodios,
                             "languages":languages})
    podcast_palabra["languages"] = [x[0] for x in podcast_palabra["languages"]]

    print(pal, podcast_palabra.shape)
    # guadamos los datos.
    podcast_palabra.to_csv("../data/raw/id_podcast/"+pal+".csv", index=False)



