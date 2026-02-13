lista_idades = [
    18, 39, 19, 44, 
    66, 33, 24, 78,
    24, 53, 32, 23,
]

# calculo media sem pandas
media = sum(lista_idades) / len(lista_idades)

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
#variancia sem pandas
diffs = 0
for i in lista_idades:
    diffs += (i - media) ** 2
variancia = diffs / (len(lista_idades)-1)

# Calculos media e variancia usando pandas
import pandas as pd

series_idades = pd.Series(lista_idades)

serie_media_idades = series_idades.mean()
serie_variancia_idades = series_idades.var()
############################################

print(media)
print(variancia)
print()
print(serie_media_idades) # usando series.mean()
print(serie_variancia_idades) # usando series.var()

############################################
print()
summary_idades = series_idades.describe()

print(summary_idades)

