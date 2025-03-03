# Práctica 1 MAIS3-BAIN: Extracción y Análisis de Datos de Twitter/X

### Requisitos
Para ejecutar los scripts es necesario instalar las siguientes dependencias:

```bash
pip install pandas regex praw emoji
```

### DataExtractor.py:
#### Descripción
*DataExtractor* es una clase en Python diseñada para procesar archivos CSV que contienen datos de Twitter/X (usando el dataset de Bitcoin provisto en la práctica) o Reddit (extraído con `ApiReddit.ipynb`). Su objetivo es extraer información clave de los tweets/posts, incluyendo:
- URLs
- Hashtags (con reglas típicas de hashtags, como por ejemplo que no puedan tener emojis o - de entremedio)
- Precios (con variedad de formatos, incluyendo $1234.56, $ 1,234.56, 1234.5$, etc.)
- Menciones (con formato @usuario para Twitter y u/usuario para Reddit)
- Emojis

Recibe como parámetros el fichero csv y el `chunksize`, que por default tiene el valor de `100000`.
El resultado se almacena en un DataFrame de pandas, con cada elemento extraído en una columna separada. Luego, se exporta como un archivo CSV para análisis en los Jupyter Notebooks:

- `Practica1_P1.ipynb` → Análisis de tweets de Twitter.
- `Practica1_P2.ipynb` → Análisis de posts de Reddit.

#### Uso
```python
from DataExtractor import DataExtractor

# Inicializar extractor con el archivo CSV de entrada
extractor = DataExtractor("data.csv", chunksize=100000)

# Procesar datos y obtener el DataFrame
df = extractor.process_text()

# Guardar los resultados en un nuevo CSV
extractor.save_file("processed_data.csv")
```

## Parte 1: Análisis de Twitter
### Practica1_P1.ipynb
Este notebook analiza los datos de Bitcoin_tweets_dataset_2.csv, el dataset proporcionado en la práctica. Sin embargo, puede utilizarse con cualquier dataset en formato CSV siempre que contenga:

- Una columna con el texto del tweet.
- Una columna con el nombre de usuario.

El único ajuste necesario para reutilizar este notebook es cambiar el nombre del CSV original y el de salida. 

#### Ejemplo de output:
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_name</th>
      <th>text</th>
      <th>Hashtags</th>
      <th>URLs</th>
      <th>Prices</th>
      <th>Emoticons</th>
      <th>Mentions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ChefSam</td>
      <td>Which #bitcoin books should I think about read...</td>
      <td>[#bitcoin]</td>
      <td>[https://t.co/32gas26rKB]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Roy⚡️</td>
      <td>@ThankGodForBTC I appreciate the message, but ...</td>
      <td>[#Bitcoin]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[@ThankGodForBTC]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ethereum Yoda</td>
      <td>#Ethereum price update: \n\n#ETH $1664.02 USD\...</td>
      <td>[#Ethereum, #ETH, #Bitcoin, #BTC, #altcoin, #c...</td>
      <td>[]</td>
      <td>[1664.02]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Viction</td>
      <td>CoinDashboard v3.0 is here\nAvailable on ios a...</td>
      <td>[#Bitcoin]</td>
      <td>[https://t.co/tMCQllv9rj]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rosie</td>
      <td>#Bitcoin Short Term Fractal (4H)💥\n\nIn lower ...</td>
      <td>[#Bitcoin, #BTC]</td>
      <td>[https://t.co/2MG9yL7SDa]</td>
      <td>[]</td>
      <td>[💥, 🫡]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>

### Análisis sobre los tweets
Notas sobre lo encontrado incluyen las siguientes:
- Los URLs son enlaces que comienzan con t.co, y son enlaces acortados de Twitter/X. Por lo tanto, son referencias a otros tweets.

## Parte 2: Análisis de Reddit
### ApiReddit.ipynb
A diferencia del análisis de Twitter, acá se requiere un paso extra previo: la extracción de posts desde la API de Reddit.

Este notebook usa la biblioteca **praw** para obtener datos del subreddit *r/Twitter*, recopilando las 1000 publicaciones más populares y guardándolas en un archivo CSV (`reddit_data.csv`), que luego será procesado por `DataExtractor.py`.

### Practica1_P2.ipynb
Este notebook es una versión duplicada de `Practica1_P1.ipynb`, pero adaptada para trabajar con los datos extraídos de Reddit. En el caso de Reddit, son mucho menos comúnes los hashtags y menciones.

#### Ejemplo de output:
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_name</th>
      <th>text</th>
      <th>Hashtags</th>
      <th>URLs</th>
      <th>Prices</th>
      <th>Emoticons</th>
      <th>Mentions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AutoModerator</td>
      <td># Greetings!\n\n&amp;;\n\nThis is the monthly "Ope...</td>
      <td>[]</td>
      <td>[https://www.reddit.com/r/Twitter/wiki/suspend...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TrueJohnWick</td>
      <td>After 3 weeks of filling out more than a dozen...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GenSkywalker98</td>
      <td>Well isn't this just great. Someone who I foll...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>venombeyond</td>
      <td>So, I'm getting this? I've had the account for...</td>
      <td>[]</td>
      <td>[https://preview.redd.it/deckrh5tzeme1.png?wid...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KingKandyOwO</td>
      <td>Twitter gives me a notification of new tweets,...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>

### Análisis sobre los posts
Notas sobre lo encontrado incluyen las siguientes:
- En Reddit se estilan mucho menos los hashtags y menciones, aunque en este caso los URLs no son mayoritariamente referencias a otros posts como en Twitter.