class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        print(f'Olá meu nome é {self.nome}!')

p1 = Pessoa('Cirilo', 'Pereira')
p2 = Pessoa('Maria', 'Joaquina')

#p1.nome = 'Cirilo'
#p1.sobrenome = 'Pereira'

#p2.nome = 'Maria'
#p2.sobrenome = 'Joaquina'





print(p1.nome)
print(p1.sobrenome)

print()
p1.falar()
print(p1)


print(p2.nome)
print(p2.sobrenome)
print()
p2.falar()

class Carro():
    def __init__(self, nomeCarro):
        self.nomeCarro = nomeCarro

    def acelerar(self):
        return 'Acelerando o carro!'


ford = Carro('Ford')

print(ford.acelerar())

print(Carro.acelerar(ford))