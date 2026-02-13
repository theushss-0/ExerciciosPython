import pandas as pd
import os 

# Limpa o terminal
def clear_terminal():
    os.system('clear')


lista_numeros = [1,7,2]
['ag1','ag2','ag3']
series_idades = pd.Series(lista_numeros)
series_idades2 = pd.Series(lista_numeros, index=['ag1','ag2','ag3'])
print(series_idades)
print(series_idades.iloc[-1])

print(series_idades2['ag1'])
print(series_idades2['ag2'])
print(series_idades2['ag3'])

clear_terminal()

numeros = {"id1": 10, "id2": 20, "id3": 30}

series_numeros = pd.Series(numeros)

print(series_numeros)
print("id1 = ",series_numeros['id1'])

