'''def somar(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [l1[i]+l2[i] for i in range(intervalo)]'''

lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4]
soma_listas = [x+y for x, y in zip(lista1,lista2)]

print(soma_listas)