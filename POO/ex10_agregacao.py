# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá ciclo de vida independente.
# seu ciclo tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relação
# onde um objeto precisa de outro para fazer determinada tarefa.
# (existem controvésias sobre as definições de agregação).


class CarrinhoCompras:

    def __init__(self):
        ## contem produtos (agregando um ou mais produtos dentro de uma lista para o objeto)
        self._produtos = []


    def total(self):
        return sum([produto.preco for produto in self._produtos]) # pega o preco de cada produto(objeto) e soma
    

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)
        #self._produtos += produtos # faz o mesmo
        """for produto in produtos:
               self._produtos.append(produto) #faz o mesmo
        """
        #print(type(produtos)) # r: tuple - *produtos == *args, é uma tupla de argumentos

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print("Nome do Produto:",produto.nome,"\tPreço: R$", produto.preco)
        print()

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


p1 = Produto('Caneta', 1.6)
p2 = Produto('Caderno', 20.0)

carrinho = CarrinhoCompras()

carrinho.inserir_produtos(p1,p2) # a agregação acontece aqui

carrinho.listar_produtos()
totalVenda = carrinho.total()

print("Preço total da venda: R$", totalVenda)