import json

caminho_arquivo = '/home/matheus/Documentos/estudos-python/ExerciciosPython/arquivos/'
nome_arquivo = 'dados_pessoa.json'
caminho_e_arquivo = f'{caminho_arquivo}{nome_arquivo}'

pessoa = {
    'nome': 'João',
    'sobrenome' : 'Pedro',
    'enderecos' : [
        {'rua': 'R1', 'numero':12},
        {'rua': 'R2', 'numero':3},
    ],
    'altura': 1.7,
    'numeros_preferidos': (1,2,3,4,5,6), ## no caso de tupas, é realizado a transformação para um array e ao transformar o arquivo novamente no programa será retornado como uma lista
    'dev':True,
    'nada': None
}


with open(caminho_e_arquivo, 'w+', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        #ensure_ascii=False, # em caso de acentuações o dump transforma com base na tabela ascii por padrão, para que não transforme, precisa informar 'false' neste parâmetro nomeado
        #indent=2 # deixa com identanção de dois espaços e realiza a quebra de linha
        )    
    
with open(caminho_e_arquivo, 'r+', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) # load() - le dos valos do json transformando em dicionário

print(type(pessoa))
print(pessoa)