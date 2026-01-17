import pessoas
import contas

class Banco:

    def __init__(self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    
    def _checar_agencia(self, conta:contas.Conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checar_cliente(self, cliente:pessoas.Pessoa):
        if cliente in self.clientes:
            return True
        
        return False
    
    def _checar_conta(self, conta:contas.Conta):
        if conta in self.contas:
            return True
        return False
    
    def _checar_conta_x_cliente(self, conta:contas.Conta, cliente:pessoas.Cliente):
        if conta is cliente.conta:
            return True
        return False
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checar_agencia(conta) and \
        self._checar_cliente(cliente) and \
        self._checar_conta(conta) and \
        self._checar_conta_x_cliente(conta, cliente)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencias!r},{self.clientes!r}, {self.contas!r})"
        return f"{class_name}{attrs}"
    

if __name__ == "__main__":
    c1 = pessoas.Cliente("Jose", 24)
    cc1 = contas.ContaCorrente(111,222)
    c1.conta = cc1

    bb1 = Banco()
    bb1.clientes.extend([c1])
    bb1.contas.extend([cc1])
    bb1.agencias.extend([222,111])

    print(c1)
    print(cc1)
    print(bb1) 
    
    print()

    print(bb1.autenticar(c1, cc1))
    