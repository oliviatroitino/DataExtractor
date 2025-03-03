import pandas as pd
import regex

class DataExtractor:
    def __init__(self, source_file: str, chunksize: int = 100000):
        """
        Inicializa el extractor con el archivo de origen.
        Parámetro:
            source_file: Ruta al archivo de datos (CSV o JSON).
            chunksize: Tamaño de los fragmentos de datos a cargar.
        """
        self.source_file = source_file
        self.data = None
        self.chunksize = chunksize

    def load_data(self):
        """
        Carga los datos y se queda con el campo del texto como "text" y el campo del usuario como "user_name".
        Elimina el resto de los campos.
        """
        try:
            data = pd.read_csv(self.source_file, usecols=['text', 'user_name'], chunksize=self.chunksize)
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def clean_text(self, text: str) -> str:
        """
        Limpia y normaliza el texto.
        Pasos sugeridos:
          - Convertir a minúsculas.
          - Eliminar caracteres especiales (no utilizados en la expresión regular) y espacios redundantes.
        Devuelve:
          El texto limpio.
        """
        if not isinstance(text, str):
            return ""
        text = regex.sub("#x200B", "", text)
        return text

    def extract_hashtags(self, text: str) -> list:
        """
        Extrae hashtags del texto.
        Parámetro:
            text: Texto de entrada.
        Devuelve:
            Lista de hashtags.
        """
        if not isinstance(text, str):
            return []
        return regex.findall(r'(?<!\w)(#[\p{L}\p{N}_]+)', text)

    def extract_urls(self, text: str) -> list:
        """
        Extrae URLs del texto.
        Parámetro:
            text: Texto de entrada.
        Devuelve:
            Lista de URLs.
        """
        if not isinstance(text, str):
            return []
        return regex.findall(r"https?://\S+", text)

    def extract_price(self, text: str) -> list:
        """
        Extrae precios del texto.
        Parámetro:
            text: Texto de entrada.
        Devuelve:
            Lista de precios.
        """
        if not isinstance(text, str):
            return []
        number = r'(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?'
        pattern = rf'(?:\$(?!\n)[ \t]?({number}))|(?:(?<=^|[^\d,\.])({number})(?=[ \t]?\$))'
        
        prices = []
        for match in regex.finditer(pattern, text):
            num = match.group(1) if match.group(1) is not None else match.group(2)
            if num:
                prices.append(float(num.replace(",", "")))
        return prices


    def extract_emoticons(self, text: str) -> list:
        """
        Extrae emoticonos del texto.
        Parámetro:
            text: Texto de entrada.
        Devuelve:
            Lista de emoticonos.
        """
        if not isinstance(text, str):
            return []
        return regex.findall(r"\p{Extended_Pictographic}+", text)

    def extract_mentions(self, text: str) -> list:
        """
        Extrae menciones del texto.
        Parámetro:
            text: Texto de entrada.
        Devuelve:
            Lista de menciones.
        """
        if not isinstance(text, str):
            return []
        return regex.findall(r"(?<=\s|^)((?:@|u/)[a-zA-Z0-9](?:[a-zA-Z0-9._]{1,13})?[a-zA-Z0-9])(?=\s|[.,!?:;]|$)(?!')", text)

    def process_text(self) -> pd.DataFrame:
        """
        Extrae todos los componentes del texto y devuelve el DataFrame procesado.
        """
        df_list = []
        for chunk in self.load_data():
            chunk = chunk.dropna(subset=['text']) # eliminar NaN

            chunk["text"] = chunk["text"].apply(self.clean_text)
            chunk["Hashtags"] = chunk["text"].apply(self.extract_hashtags)
            chunk["URLs"] = chunk["text"].apply(self.extract_urls)
            chunk["Prices"] = chunk["text"].apply(self.extract_price)
            chunk["Emoticons"] = chunk["text"].apply(self.extract_emoticons)
            chunk["Mentions"] = chunk["text"].apply(self.extract_mentions)
            df_list.append(chunk)
        self.df_data = pd.concat(df_list, ignore_index=True)
        return self.df_data

    def save_file(self, file_name: str) -> None:
        """
        Guarda el DataFrame resultante como un archivo CSV.
        Parámetro:
            file_name: Nombre del archivo de salida (sin extensión).
        """
        if self.df_data is None:
            self.process_text()
        self.df_data.to_csv(file_name + ".csv", index=False)
