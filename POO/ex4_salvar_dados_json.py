import json

CAMINHO_ARQUIVO = './arquivos/dd_pessoa.json'

class Pessoa:


    def __init__(self, nome, sobrenome, idade, peso, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def SalvarJson(self, listaDados=[]):

        listaDados.append(self.__dict__)

        with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
            json.dump(
                listaDados,
                arquivo,
                ensure_ascii=False,
                indent=2
            )

    def CarregarDadosJson():
        
        try:
            with open(Pessoa.CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
                return list(json.load(arquivo))
        except:
            return []
        
        
'''
InfoPessoa = Pessoa('José', 'Pereira', 64, 82.4, 1.8)

InfoPessoa.SalvarJson(Pessoa.CAMINHO_ARQUIVO, list(Pessoa.CarregarDadosJson(Caminho=Pessoa.CAMINHO_ARQUIVO)))
'''