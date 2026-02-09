lista_idades = [
    18, 39, 19, 44, 
    66, 33, 24, 78,
    24, 53, 32, 23,
]

"""
media = sum(lista_idades) / len(lista_idades)

diffs = 0

for i in lista_idades:
    diffs += (i - media) ** 2
    
#print(diffs)
##print(len(lista_idades))
#print(sum(lista_idades))
#variancia = diffs / (len(lista_idades)-1)

#print('Média: ', media)
#print('Variancia: ', variancia)
"""


import pandas as pd

series_idades = pd.Series(lista_idades)

print(series_idades)