class Pessoa:

    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade
    



p1 =  Pessoa('José', 25)

print(p1.__dict__)
print(vars(p1))
print()

p1.__dict__['outra'] = 'Oxe'
print(p1.__dict__)
del p1.__dict__['outra']

dados = p1.__dict__
p2 = Pessoa(**dados)




