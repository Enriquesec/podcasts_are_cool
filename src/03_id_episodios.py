import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# credenciales
client_id = 'XXXXXX'        
client_secret = 'XXXX'       

# nos conectamos a la api
client_credentials_manager = SpotifyClientCredentials( client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, language="es", 
                    requests_timeout=30, retries=10)

# cargamos los id de los podcast y filtramos los que no tengan episodios
id_podcast = pd.read_csv("../data/processed/podcats_en_espanol.csv")
id_podcast = id_podcast[id_podcast.episodios>0] 


# inicializamos las listas a ocupar.
description = []
duration = []
id_episodio = []
language = []
name = []
release_date = []
typ = []
name_podcast = []
publiser = []
id_publiser = []
total_episodios = []


for i in range(0, id_podcast.shape[0]): # iteramos por todos los id de los podcasts.
    for num in range(0, id_podcast.loc[i,"episodios"], 50): # iteramos por el numero de episodios
        try:
            episodios = sp.show_episodes(show_id=id_podcast.loc[i, "id_list"], limit=50, offset=num, 
                                     market="MX") # realizamos la consulta
        except:
            next
        for p, t in enumerate(episodios["items"]):
            # agregamos la informacion
            total_episodios.append(id_podcast.loc[i,"episodios"])
            name_podcast.append(id_podcast.loc[i, "name"])
            publiser.append(id_podcast.loc[i, "fecha"])
            id_publiser.append(id_podcast.loc[i, "id_list"])
            description.append(t["description"])
            duration.append(t["duration_ms"])
            id_episodio.append(t["id"])
            language.append(t["language"])
            name.append(t["name"])
            release_date.append(t["release_date"])
            typ.append(t["type"])
    if (i%100)==0:
        print(i)
        
# creamos el dataframe con todos los capitulos
cap_complete = pd.DataFrame({'name_podcast':name_podcast, "publiser":publiser, "id_publiser":id_publiser, "total_episodios":total_episodios,
                         "description":description, "duration":duration, "id_episodio": id_episodio,
                         "language":language, "name_episodio":name, "release_date":release_date,
                         "type":typ})

# guardamos el dataframe procesado.
cap_complete.to_csv("../data/processed/episodios/cap_complete.csv", index=False)



