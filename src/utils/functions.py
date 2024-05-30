import re
import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer

def data_preprocessing(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'\[.*?\]|@\w+\s*|https?://\S+|www\.\S+|http|\w*\d\w*|<.*?>+|[%s\n]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', '', text)
    return text

def limpieza_texto(df):

    df_res = df.copy()
    df_res['text_combined'] = df['text_combined'].apply(data_preprocessing)
    df_res.rename(columns={'text_combined': 'body','label':'label'},inplace=True)
    return df_res

def palabras_mas_comunes(df, npalabras):

    vectorizer_count = CountVectorizer(max_features=npalabras, stop_words='english')
    textos = df['body'].tolist()
    textos = vectorizer_count.fit_transform(textos)
    vocabulario = vectorizer_count.vocabulary_
    palabras_mas_comunes = {palabra: textos[:, indice].sum() for palabra, indice in vocabulario.items()}
    palabras_mas_comunes = sorted(palabras_mas_comunes.items(), key=lambda x: x[1], reverse=True)
    print("Palabras más comunes:")
    for palabra, frecuencia in palabras_mas_comunes:
        print(f'{palabra}: {frecuencia}')