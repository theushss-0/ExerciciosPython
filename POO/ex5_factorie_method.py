#Factorie Method

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #define um metodo de instancia para o objeto (Metodo da instancia do objeto - self)
    def get_pessoa(self):
        return f"{self.nome} tem {self.idade} de idade!"

    #define uma classe que cria um objeto (Metodo da classe - cls)
    @classmethod
    def criar_pessoa(cls,nome, idade):
        return cls(nome, idade)
    


p1 = Pessoa('Jorge', 44)# criou o objeto instanciando a propria classe
p2 = Pessoa.criar_pessoa('Maria', 33) # criou o objeto com a função criar_pessoa que instancia a classe

print(p2.nome, " tem ", p2.idade, "de idade!")
print(p1.nome, " tem ", p1.idade, "de idade!")


print(p2.get_pessoa())
print(p1.get_pessoa())

pn = p1.criar_pessoa(p2.nome, p2.idade) 

print(pn.nome)

