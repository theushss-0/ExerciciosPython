import csv
from pathlib import Path

CAMINHO_CSV= Path(__file__).parent / "testes/teste.csv"

print(CAMINHO_CSV)

lista_dict = [
    {'nome': "José", "idade":24},
    {'nome': "Maria", "idade":55},
    {'nome': "Laura", "idade":45},
]

print(lista_dict[0].keys())

#with open(CAMINHO_CSV, 'w') as arquivo:
#    nome_colunas = lista_dict[0].keys()
#    escritor = csv.writer(arquivo)

#    escritor.writerow(nome_colunas)
    
#    print()
#    for clientes in lista_dict:
#        escritor.writerow(clientes.values())


with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_dict[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    #escritor.writerow(cliente for cliente in lista_dict) // dá erro

    #escritor.writerows(cliente for cliente in lista_dict) // forma correta writerow's'(list_comprehention)

    for cliente in lista_dict:
       escritor.writerow(cliente)