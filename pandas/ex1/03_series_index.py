import pandas as pd

lista_idades = [
    18, 39, 19, 44, 
    66, 33, 24, 78,
    24, 53, 32, 23,
]

series_idade = pd.Series(lista_idades) 
print(series_idade)

print(series_idade[0]) ## as series funcionam como um dicionário, [0] é a chave 0 da serie
print(type(series_idade.__dict__))
dict_idades = dict(series_idade)
print(dict_idades)

series_idades = series_idade.sort_values()

print(series_idades)