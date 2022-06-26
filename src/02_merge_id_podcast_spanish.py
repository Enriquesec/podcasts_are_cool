# cargamos las librerias
import pandas as pd
import numpy as np

# leemos los archivos en cierta ubicacion
paths = os.listdir("../data/raw/id_podcast")

# inicializamos un dataframe
id_podcast = pd.DataFrame(columns=['name', 'id_list', 'fecha', 'episodios', 'languages'])

# cargamos los archivos de los id podcasts.
for path in paths:
    podcast = pd.read_csv("../data/raw/id_podcast/"+path)
    id_podcast = pd.concat([id_podcast, podcast])

# eliminamos duplicados y seleccionamos los que son en espanol
id_podcast = id_podcast.drop_duplicates("id_list")
id_podcast = id_podcast[id_podcast.languages.str.startswith("es", na = False)]

# escribimos el dataframe procesado
id_podcast.to_csv("../data/processed/podcats_en_espanol.csv", index=False)
