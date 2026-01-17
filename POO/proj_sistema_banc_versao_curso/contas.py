import abc

class Conta(abc.ABC):

    def __init__(self, agencia: int, conta:int , saldo:float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    
    @abc.abstractmethod
    def sacar(self, valor:float)-> float: ...

    def depositar(self, valor:float)->float:
        self.saldo+= valor
        self.detalhes(f"(DEPÓSITO de R$ {valor}) ")
        return self.saldo

    def detalhes(self, msg:str = ''):
        print(f"O seu saldo é R$ {self.saldo} {msg}")




class ContaPoupanca(Conta):

    def sacar(self, valor:float)->float:
        saldo_suficiente = self.saldo - valor

        if saldo_suficiente >= 0:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print("Saldo é insuficiente para realizar esta operação!")
        self.detalhes(f"(SAQUE NEGADO {valor})")
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r},{self.conta!r}, {self.saldo!r})"
        return f"{class_name}{attrs}"


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo:float=0, limite:float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    
    def sacar(self, valor:float)->float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"(SAQUE {valor})")
            return self.saldo
        
        print("Seu saldo é insuficiente!")
        print(f"seu limite é {limite_maximo}")
        self.detalhes(f"(SAQUE NEGADO {valor})")
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r},{self.conta!r}, {self.saldo!r},"\
            f" {self.limite!r})"
        return f"{class_name}{attrs}"



if __name__ == "__main__":
    #cp1 = ContaPoupanca(111,222, 0)
    #cp1.sacar(1)
    #cp1.depositar(100)
    #cp1.sacar(10)
    cc1 = ContaCorrente(222,333,0,200)
    cc1.sacar(199)
    cc1.sacar(2)
