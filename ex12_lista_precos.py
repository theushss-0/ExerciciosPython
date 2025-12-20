from copy import deepcopy
from dados import produtos

print("Produtos Originais: \n")
print(*produtos, sep='\n')
print()

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**produto,'preco': round(produto['preco'] * 1.1, 2)}
    for produto in deepcopy(produtos)
]

print("\nNovos Produtos com preço alterado(aumento de 10%):")
print()
print(*novos_produtos, sep="\n")

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    deepcopy(produtos), 
    key=lambda item: item['nome'],
    reverse=True
)

print("\nProdutos Ordenados por nome:")
print()
print(*produtos_ordenados_por_nome, sep="\n")

#Ordene os produtos por preco crescente (do menor para o maior)
#gere produtos_ordenados_por_preco por deep copy (copia profunda)
produtos_ordenados_por_preco = sorted(
    deepcopy(produtos),
    key= lambda item: item['preco'],
    reverse=False
)

print("\nProdutos Ordenados por Preço:")
print()
print(*produtos_ordenados_por_preco, sep="\n")
