# Práctica 1 MAIS3-BAIN: Extracción y Análisis de Datos de Twitter/X

### Requisitos:
- Python 3.x
- Regex
- Pandas
- praw (para la extracción desde Reddit)

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
En *Practica1_P1.ipynb*, se analiza el fichero *Bitcoin_tweets_dataset_2.csv* dado para la práctica, pero funciona con cualquier dataset csv del que se pueda extraer una columna de texto y una de usuario/autor. El único cambio entre este fichero y el *Practica1_P2* es el nombre del csv original y el csv que sale del df.

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
    <tr>
      <th>5</th>
      <td>AkinHack</td>
      <td>Y’all Message me for any account recovery or h...</td>
      <td>[#CYBER, #security, #Coinbase, #Bitcoin, #BNB,...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CAIR (Pump/Dump)</td>
      <td>PUMP : 4-Hour Chart (1x!) (NORMAL)\nCoin    : ...</td>
      <td>[#FILUSDT, #FIL, #Bitcoin]</td>
      <td>[https://t.co/zKtYat6duH]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NFTevening</td>
      <td>📰TwelveFold by @yugalabs Unveils Unique #Bitco...</td>
      <td>[#Bitcoin, #NFTs]</td>
      <td>[https://t.co/UqSa1MkQiJ]</td>
      <td>[]</td>
      <td>[📰, 🟣, 🟣]</td>
      <td>[@yugalabs]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>AbdeL</td>
      <td>@BitcoinBullsNFT The first my #NFT in  #Bitcoi...</td>
      <td>[#NFT, #Bitcoin]</td>
      <td>[https://t.co/hO6t69frCZ]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[@BitcoinBullsNFT]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PUBLORD</td>
      <td>Your first #Bitcoin Halving will age and humbl...</td>
      <td>[#Bitcoin]</td>
      <td>[https://t.co/U6JwlLNlMg]</td>
      <td>[]</td>
      <td>[😉😂]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>

## Parte 2: Análisis de Reddit
### ApiReddit.ipynb
El análisis de Reddit tiene un paso extra previo comparado con el proceso de análisis de Twitter, el cual es extraer posts de la api de Reddit con el fichero *ApiReddit.ipynb*. Este fichero utiliza la biblioteca *praw* para extraer datos de Reddit, específicamente del subreddit *r/Twitter*. Su objetivo es recopilar publicaciones y guardar la información en un archivo CSV para su posterior análisis.

### Practica1_P2.ipynb

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
    <tr>
      <th>5</th>
      <td>betimd</td>
      <td>I bought premium account and my profile shows ...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Murky-Perception-349</td>
      <td>Trying to view an account with tweets that has...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Rok_Horvat_14</td>
      <td>I do a lot of liking on Twitter/X &amp; I want to ...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>CobolCoder1983</td>
      <td>I've reported literally hundreds of them but i...</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>vincentsigmafreeman</td>
      <td>Will X premium on web sync with my app…</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>