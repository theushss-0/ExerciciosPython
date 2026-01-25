# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
#
# Lifo  e fifo
# pilha e fila

# LIFO (Last In First Out)
# Pilha (stack)
# Significa que o último item a entrar será o primeiro a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
# Vídeo:
# https://youtu.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(n) Tempo Linear

print('-------- LIFO')
lista = [0,1,2,3,4,5,6,7,8,9]
print()
print(lista)
# ✅ Legal (LIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(10)
print(lista," -> INSERE NO FINAL")

#  0  1  2  3  4  5  6  7  8  9  10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.append(11)
print(lista," -> INSERE NO FINAL")


#  0  1  2  3  4  5  6  7  8  9  10, 11
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print()
print('Último da lista:', lista[-1])
print("Lista: ", lista)

print()

ultimo_removido = lista.pop()
print(lista," -> ROMOVE NO FINAL")
ultimo_removido = lista.pop()
print(lista," -> ROMOVE NO FINAL")
print()

print("Útimo removido: ", ultimo_removido)
print('Último da lista:', lista[-1])
print("Lista: ", lista)

print()
print('-------- FIFO')
print()
print(lista)
# 🚫 Ruim (FIFO com lista)
#  0  1  2  3  4  5  6  7  8  9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(0,10)

print(lista," -> INSERE NO INICIO")


#   0  1  2  3  4  5  6  7  8  9, 10
# [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.insert(0,11)
print(lista," -> INSERE NO INICIO")

#  0   1   2  3  4  5  6  7  8  9, 10 11
# [11, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()
print('Último da lista:', lista[-1])
print("Lista: ", lista)

print()

ultimo_removido = lista.pop(0)
print(lista," -> REMOVE NO INICIO")

ultimo_removido = lista.pop(0)
print(lista," -> REMOVE NO INICIO")
print()



print("Útimo removido: ", ultimo_removido)
print('Último da lista:', lista[-1])
print("Lista: ", lista)

