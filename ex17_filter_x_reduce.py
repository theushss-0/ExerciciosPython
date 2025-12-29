from copy import deepcopy
from functools import reduce
# filter é um filtro funcional

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

#  Função para verificar o preço do produto atual
def verificar_preco(produto):
    return produto['preco'] > 10

def soma_valores(acumulador, produto):
    return acumulador + produto['preco']

tab_precos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90}
]

# -> Com  list Comprehension

# novos_produtos = [
#     p for p in deepcopy(tab_precos)
#     if p['preco'] > 20
# ]

# -> Com a função filter

produtos_maior_que_dez = filter(
    ##lambda produto: produto['preco'] >  10, 
    verificar_preco,
    tab_precos
)

preco_total_list = round(reduce(
    lambda ac,prod: prod['preco'] + ac,
    #soma_valores,
    tab_precos,
    0
),2)

print("Preços total dos itens: ",preco_total_list)

print_iter(produtos_maior_que_dez)