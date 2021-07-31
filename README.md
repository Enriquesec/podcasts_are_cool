# Podcasts are cool
Analizaremos el comportamiento de los podcast que se encuentran en Spotify en idioma español. En un comienzo se tenía pensado analizar solo los podcasts que se crean en México, pero por cuestiones de los datos proporcionados de la API no es posible. Por lo cuál, el análisis planteado se realizará de manera general.

Tenemos varios objetivos planteados:
- Queremos ver la distribución del número de episodios en los podcasts que actualmente se transmiten.
- Número de podcasts activos, creados y abandonados diarios. 
- Ver la interacción entre los podcasts y los invitados.

Para el último objetivo, se necesita un análisis más riguroso.


## Datos.
Primero realizamos una busqueda de las siguientes palabras clave en la API de Spotify:
	- leyenda, creativo, datos, comedia, cultura, idioma, musica, mente, escuelas, libros, noticias, deportes, tecnología, comida, tacos, educacion, politica, 
	negocios, autoayuda, historia, finanzas, arte, entretenimiento, terror, novelas, juegos, ajedrez, salud, nutricion.
Con los resultados de la busqueda anterior obtuvimos los id's de los podcasts en español. Posteriormente para cada id descargamos la informacion de cada uno de sus épisodios emitidos.

Definimos la *fecha de creación* del podcasts como la fecha en la cual se emitio el primer episodio, la *fecha de abandono* como la fecha del último podcastas emitido más un lapso de 7 semanas. Con estas dos fechas procedimos a calcular el número de podcasts emitidos acumulados, el número de podcasts activos y el número de podcasts abandonados.

*Ver los notebooks:*
- [01_scrapper_id_spotify.ipynb](notebooks/01_scrapper_id_spotify.ipynb)
- [03_scrapper_id_episodios.ipynb](notebooks/03_scrapper_id_episodios.ipynb)

*NOTA: Los datos analizados no son todos los que se encuentran en la API de Spotify, es decir, se trabajo con una muestra de todos los podcasts. Y no se esta seguro que tan representativa es esta muestra obtenida, pero para reducir la diferencia podríamos buscar más palabras claves en la API  de Spotify para tener un mayor porcentaje de información.*

## Análisis.
Los resultados preliminares se puede ver en:
- [04_analisis_visual.ipynb](notebooks/04_analisis_visual.ipynb)

Las animaciones de los episodios y de los podcasts se realizaron con el notebook:
- [05_animation.ipynb](notebooks/05_animation.ipynb)

*NOTA IMPORTANTE: para no violar los términos y condiciones del uso de la API de Spotify, nos abstenemos a guardar los datos ocupados y de ampliar el análisis a simples visualizaciones de los datos.*