# Práctica 1 MAIS3-BAIN: Extracción y Análisis de Datos de Twitter/X

## Requisitos generales:
- Python 3.x
- Regex
- Pandas

## DataExtractor.py:

### Descripción
*DataExtractor* es una clase en Python diseñada para procesar archivos CSV que contienen datos de Twitter/X (csv de Bitcoin dado para la práctica) o Reddit (csv extraído de la API de Reddit). Su objetivo es extraer información clave de los tweets/posts, incluyendo:
- URLs
- Hashtags
- Precios
- Menciones
- Emojis
El resultado del procesamiento se almacena en un DataFrame de pandas, con cada tipo de elemento extraído en una columna separada. Posteriormente, este DataFrame se exporta a un archivo CSV en los Jupyter Notebooks *Practica1_P1.ipynb* (Tweets) y *Practica1_P2.ipynb* (Reddit Posts).

### Uso
```python
from DataExtractor import DataExtractor

# Inicializar extractor con el archivo CSV de entrada
extractor = DataExtractor("tweets.csv")

# Procesar datos y obtener el DataFrame
df = extractor.process_text()

# Guardar los resultados en un nuevo CSV
extractor.save_file("tweets_procesados")
```

## Practica1_P1.ipynb
### Ejemplo de output:
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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