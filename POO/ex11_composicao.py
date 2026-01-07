"""
Relações entre classes: associação, agregação e composição

Composição é uma especialização de agregação.
Mas nela, quando o objeto 'pai' for apagado (cliente), todas 
as referências dos objetos filhos também são apagadas.

"""
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = [] # lista de endereços


    def inserir_enderecos(self, endereco):
        self.enderecos.append(endereco) # nesse momento acontece a composição
    
    def listar_enderecos(self):
        print('Cliente: ', self.nome)
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

        print()

    def __del__(self):
        print("APAGANDO, ", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    # AO FINALIZAR O PROGRAM OS DADOS DO CLIENTE SÃO APAGADOS DA MEMÓRIA
    # OU AO CHAMAR O DEL NO OBJETO
    def __del__(self):
        print("APAGANDO, ", self.rua, self.numero)



cliente = Cliente('José')

cliente.inserir_enderecos(Endereco('Rua A', 1123))
cliente.inserir_enderecos(Endereco('Rua B', 11))
endereco = Endereco('RUA N', 1) #Este endereço existe até que o programa finalize ou o objeto seja deletado (del endereco)
cliente.listar_enderecos()
cliente.inserir_enderecos(endereco)

del cliente # 

print("#### FIM PROGRAMA")