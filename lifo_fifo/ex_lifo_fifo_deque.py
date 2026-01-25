from collections import deque

# FIFO (First In First Out)
# Filas (queue)
# Significa que o primeiro item a entrar será o primeiro a sair (deque)
# Artigo:
# https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/
# Vídeo:
# https://youtu.be/RHb-8hXs3HE
# Para tirar itens do final: O(1) Tempo constante
# Para tirar itens do início: O(1) Tempo constante

# ✅ Legal (FIFO com deque)


fila_correta: deque[int] = deque()

fila_correta.append(3) #adicionando ao final
print(fila_correta, "-> INSERINDO NO FINAL")
fila_correta.append(4) #adicionando ao final
print(fila_correta, "-> INSERINDO NO FINAL")
fila_correta.append(5) #adicionando ao final
print(fila_correta, "-> INSERINDO NO FINAL")

print()

fila_correta.appendleft(0) # adicionando no inicio
print(fila_correta, "-> INSERINDO NO INICIO")
fila_correta.appendleft(1) # adicionando no inicio
print(fila_correta, "-> INSERINDO NO INICIO")
fila_correta.appendleft(2) # adicionando no inicio
print(fila_correta, "-> INSERINDO NO INICIO")

print()

fila_correta.pop() # 5
print(fila_correta, "-> REMOVENDO NO FINAL")

fila_correta.popleft() # 2
print(fila_correta, "-> REMOVENDO NO INICIO")