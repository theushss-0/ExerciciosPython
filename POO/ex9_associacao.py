class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

    

class Ferramenta:
    def __init__(self, nome_ferramenta):
        self.nome_ferramenta = nome_ferramenta
    
    def escrever(self):
        return 'Estrou escrevendo!'
    


escritor = Escritor("José") # criou um objeto de Escritor (classe-molde)
ferramenta = Ferramenta("Caneta Bic") # criou um objeto de Ferramenta (classe-molde)

"""
Quando um Objeto possui um atributo que receber um outro objeto e a partir deste utilizar funcionalidades e atributos presente neste outro objeto, é chamada de associação
"""

escritor.ferramenta = ferramenta  ## nesse momento está acontecendo uma associação

print(escritor.ferramenta.escrever()) ## utilizando a partir do escritor um médodo (funcionalidade) de uma ferramenta(no caso a caneta)

