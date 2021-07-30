# Podcasts are cool
Analizaremos el comportamiento de los podcast que se encuentran en Spotify en idioma español. En un comienzo se tenía pensado analizar solo los podcasts que se crean en México, pero por cuestiones de los datos proporcionados de la API no es posible. Por lo cuál, el análisis planteado se realizará de manera general.

Tenemos varios objetivos planteados:
- Queremos ver la distribución del número de episodios en los podcasts que actualmente se transmiten.
- Número de podcasts activos, creados y avandonados diarios. 
- Ver la interacción entre los podcasts y los invitados.

Para el último objetivo, se necesita un análisis más riguroso.


## Datos.
Primero realizamos una busqueda de ciertas palabras claves en la API, con el objetivo de obtener los id's de los podcasts en español. Posteriormente para cada id descargamos la descripción de cada uno de sus épisodios emitodos. 
*Ver los notebooks:*
- [01_scrapper_id_spotify.ipynb](notebooks/01_scrapper_id_spotify.ipynb)
- [03_scrapper_id_episodios.ipynb](notebooks/03_scrapper_id_episodios.ipynb)

## Análisis.
Los resultados preliminares se puede ver en:
- [04_analisis_visual.ipynb](notebooks/04_analisis_visual.ipynb)

*NOTA: para no violar los términos y condiciones del uso de la API de Spotify, nos abstenemos a guardar los datos ocupados y de ampliar el análisis a simples visualizaciones de los datos.*