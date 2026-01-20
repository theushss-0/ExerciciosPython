# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0) # não muda nada

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10,20,3)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
#r_int = random.randint(10, 20)
r_int = random.randint(1,20)
print(r_int)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
#r_uniform = random.uniform(10, 20)
r_uniform = round(random.uniform(0,1), 4) #randomiza numeros com ponto flutuante
print(r_uniform)
# print(r_uniform)


nomes = ["Maria", 'José', 'João', "Ana"]
random.shuffle(nomes) # muda a lista original

print(nomes)

sample_nomes = random.sample(nomes, k=2) # emparalha aleatóriamente os valores da lista e pega a quantidade 
                                         # de armundos passados no parametro 'k' para uma nova lista.

print(sample_nomes)

choise_nomes = random.choices(nomes, k=2) #pode haver repetição de valores
print(choise_nomes)
