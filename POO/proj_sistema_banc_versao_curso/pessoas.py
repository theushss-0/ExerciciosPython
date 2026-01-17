import contas
class Pessoa:

    def __init__(self, nome:str, idade:int)->None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome:str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade



class Cliente(Pessoa):

    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self._conta: contas.Conta | None = None

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta:contas.Conta):
        self._conta = conta
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.nome!r},{self.idade!r})"
        return f"{class_name}{attrs}"


if __name__ == "__main__":
    c1 = Cliente("Jose", 24)
    c1.conta = contas.ContaPoupanca(123,123,0,0)
    print(c1)
    print(c1.conta)    
    

    

        