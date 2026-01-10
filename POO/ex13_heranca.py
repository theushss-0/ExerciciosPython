class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def falar_alguma_coisa(self):
        print("Na classe pessoa:")
        return f"Olá {self.nome}!"


class Cliente(Pessoa):
    def falar_alguma_coisa(self):
        print(f"Na classe cliente!")
        return f"Olá {self.nome}!"
    


class Funcionario(Pessoa):
    pass



p1 = Cliente("Matheus", "Silva")
retorno1 = p1.falar_alguma_coisa()
print(retorno1)

p2 = Funcionario("Matheus", "Silva")
retorno2 = p2.falar_alguma_coisa()
print(retorno2)