
import pandas as pd
import numpy as np
from art import *
import os

os.system('cls' if os.name == 'nt' else 'clear')

df = pd.read_csv('synergy_logistics_database.csv')

# imprimir dataframe
tprint("Dataframe")
tprint("HEAD")
print(df.head())

# imprimir su información general
tprint("info")
print(df.info())

# basarnos en valor final y generar nuevo DataFrame en base a Destino
by_country = df.filter(['destination', 'total_value'], axis=1)
by_country = by_country.rename(columns={"total_value": "VALOR_TOTAL"})
tprint("By Destination")
by_country = by_country.groupby('destination')

# Imprimir valor por suma
tprint("TOTAL SUMA")
print(by_country.sum())

# Imprimir por promedio
tprint("PROMEDIO")
print(by_country.mean())

# imprimir por Desviación Estándar
tprint("Desviacion")
tprint("Estandar")
print(by_country.std())

# Imprimir por valor máximo
tprint("VALOR MAXIMO")
print(by_country.max())

# Imprimir por valor máximo
tprint("VALOR MINIMO")
print(by_country.min())

# Imprimir conteo
tprint("CONTEO")
print(by_country.count())

# Imprimir descripción
tprint("DESCRIPCION")
print(by_country.describe().iloc[:,0:7])

#by_country.plot.hist(bins=12, alpha=0.5)
