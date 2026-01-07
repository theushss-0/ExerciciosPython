################################

# @property
# @attr.setter

################################

"""
ao utilizar o decorador @property a uma método, esta ganha um comportamento de atributo.
- A primeira função que tem o decorador @property, retorna o valor (realiza um getter)
- Nesse momento não é possível a atribuição

Para que também seja possível atribuir um valor a essa @property, é necessário criar uma segunda função.
- na função é necessario informar um decorador nomeado com o nome da @property, ex, def cor(), nesse caso a "cor" é o nome dessa @property então @cor seguido de .setter que indica que esta função realiza a atribuição do valor, então o nome ficaria @cor.setter, e em seguida incia a função
- na função, precisa receber como parâmetro o self e o valor que será atribuido a este atributo

@cor.setter
def cor(self, cor):
    self._cor = cor

isso torna possível que o atributo 'cor' receba um valor atravez da função sem ter que chamar o nome do atributo diretamente (self._cor)
"""



class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    # o '@Property' faz com que a função se comporte como um atributo (getter)
    @property
    def cor(self):
        print("PROPERTY - getter")
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        print("do Property cor - SETTER")
        self._cor = cor

    # o Property não está amarrado ao atributo, é possível utiliza-lo para fazer algo que não tem a ver com o atributo em sí.
    '''
    @property
    def cor_tampa(self):
        return 'Qualquer Coisa'

    '''

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, cor_tampa):
        self._cor_tampa = cor_tampa



    
    


c1 = Caneta("Azul")
#c1.cor_caneta = 'Preto' # não pode atribuir o valor ao atributo devido ele ser especifico para retorno (realiza apenas um getter do attr)
#Agora é possível realizar a atribuição de um valor ao objeto

c1.cor = 'Roxo'
c1.cor_tampa = 'Amarelo'


print(c1.cor)

print(c1.cor_tampa)