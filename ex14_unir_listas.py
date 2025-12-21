# Exercício - Unir Listas

# Crie uma funcao zipper (como zipper de roupas)
"""
O trabalho dessa função será unir duas listas na ordem

ex: 
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', ''MG)]

"""

'''def decorador(funcao):

    def executa_funcao(*args, **kwargs):
        res = funcao(*args, **kwargs)
        return res
    return executa_funcao


@decorador'''

'''
def mapeia_listas(lista_cidades, lista_estados):
    intervalo = min(len(lista_cidades), len(lista_estados))
    return [(lista_cidades[i], lista_estados[i]) for i in range(intervalo)]'''

from itertools import zip_longest

lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']

lista_cidade_x_estado = zip(lista_cidades, lista_estados)
lista_maior = zip_longest(lista_cidades,lista_estados)

print(list(lista_cidade_x_estado))
print(list(lista_maior))
    
