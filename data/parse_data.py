# -*- coding: utf-8 -*-

import pandas as pd
import json
import numpy as np
import unidecode

# Abrir el archivo en pandas
df = pd.read_csv('10000_formas.txt', sep='\t', encoding='latin-1', skipinitialspace=True)

df['Orden'] = df['Orden'].str.lower()  # Convertir a minúsculas
df['Orden'] = df['Orden'].str.strip()  # Convertir a minúsculas
df['Orden'] = df['Orden'].str.replace('[^\w\s]', '')  # Eliminar caracteres no alfanuméricos
df['Orden'] = df['Orden'].apply(unidecode.unidecode)  # eliminar tildes

# Filtrar palabras de solo 5 letras
words = df['Orden'].to_numpy()
count = np.vectorize(len)(words)
fiveLetterWord = words[count==5]

# Serializar el array a formato JSON
json_string = json.dumps(fiveLetterWord.tolist(), ensure_ascii=False).encode('utf8')
with open('../src/words_data.js', 'w', encoding='utf-8') as f:
    f.write("export const words = " + json_string.decode() + ";")