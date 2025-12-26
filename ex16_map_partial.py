from functools import partial
from types import  GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


def muda_precos_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

aumentar_dez_porcento = partial(
    aumentar_porcentagem, # função do processamento
    porcentagem = 1.1 # parametro da função
)

tab_precos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90}
]


'''novos_produtos = [
    {**p,'preco': aumentar_dez_porcento(p['preco'])} for p in tab_precos
]'''

novos_produtos = list(map(muda_precos_produtos, tab_precos))
# map - retorna um objeto do tipo map
print(novos_produtos) # Itera sobre os valores de novos_produtos

#novos_produtos = (x for x in range(10))
print_iter(novos_produtos)
print_iter(novos_produtos)# após ter percorrido uma vez, o objeto é esgotado, não sendo mais possível iterar


generator_ = (x for x in range(10))
#print(list(novos_produtos))

print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))

print(isinstance(generator_, GeneratorType))
