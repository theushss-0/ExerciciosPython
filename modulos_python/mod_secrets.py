import secrets

#print(secrets.randbelow(100))
#print(secrets.choice([1,4,5,65,67,7]))

random = secrets.SystemRandom()

r_choices = random.choices([1,2,2,3,4,45,65,], k=3)
print(r_choices)

r_range = random.randrange(10, 40,3)
print(r_range)

lista_nomes = ['Maria', 'José', "João", "Ana"]
random.shuffle(lista_nomes)
print(lista_nomes)

r_nomes = random.sample(lista_nomes,k=3)
print(r_nomes)

r_int = random.randint(1,1000)
print(r_int)

r_uniform = random.uniform(0,1)
print(r_uniform)
