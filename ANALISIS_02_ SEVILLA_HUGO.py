
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

by_country = df.filter(['direction','origin','destination','total_value'], axis=1)
by_country = by_country.rename(columns={"direction":"DIRECCION","origin":"ORIGEN","destination":"DESTINO","total_value": "VALOR_TOTAL"})

by_country = by_country.groupby(['DIRECCION', 'ORIGEN', 'DESTINO'])
tprint("groupby")
print(by_country.head())

#Imprimir valor por suma
tprint("TOTAL SUMA")
print(by_country.sum().iloc[:60])
print(by_country.sum().iloc[60:120])
print(by_country.sum().iloc[120:180])
print(by_country.sum().iloc[180:])

# Imprimir por promedio
tprint("PROMEDIO")
print(by_country.mean().iloc[:60])
print(by_country.mean().iloc[60:120])
print(by_country.mean().iloc[120:180])
print(by_country.mean().iloc[180:])

input('ENTER para continuar... ')
os.system('cls' if os.name == 'nt' else 'clear')

# imprimir por Desviación Estándar
tprint("Desviacion")
tprint("Estandar")
print(by_country.std().iloc[:60])
print(by_country.std().iloc[60:120])
print(by_country.std().iloc[120:180])
print(by_country.std().iloc[180:])

# Imprimir por valor máximo
tprint("VALOR MAXIMO")
print(by_country.max().iloc[:60])
print(by_country.max().iloc[60:120])
print(by_country.max().iloc[120:180])
print(by_country.max().iloc[180:])

# Imprimir por valor máximo
tprint("VALOR MINIMO")
print(by_country.min().iloc[:60])
print(by_country.min().iloc[60:120])
print(by_country.min().iloc[120:180])
print(by_country.min().iloc[180:])

# Imprimir conteo
tprint("CONTEO")
print(by_country.count().iloc[:60])
print(by_country.count().iloc[60:120])
print(by_country.count().iloc[120:180])
print(by_country.count().iloc[180:])

# Imprimir descripción
tprint("DESCRIPCION")
print(by_country.describe().transpose())