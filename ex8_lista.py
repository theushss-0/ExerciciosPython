"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o pograma quebre com
erros de índices inexistentes na lista
"""
import os

painel_options = """
O que deseja fazer?
[I]nserir novo item\t[A]pagar item\t[L]istar os itens da lista\t[S]air
"""

def listar_item(lista):
    for indice,valor in enumerate(lista):
        print(indice,"-", valor)

lista_compras = []
list_options = ('I' , 'A', 'L', 'S')


while True:

    option = input(f"{painel_options}\n=> ").upper()
    
    if(not option or option not in list_options):
        os.system('clear')
        print("Você precisa informar uma das Opções válidas!!! Tente Mais uma vez.")
        continue
    
    if(option == list_options[3]):
        os.system('clear')
        print("Até uma proxima vez!!!")
        break

    if(option == list_options[0]):
        os.system('clear')
        lista_compras.append(str(input("Informe o nome do produto\n=> ")))
        print(f"Produto {lista_compras.index(lista_compras[-1])} - {lista_compras[-1]} inserido com sucesso.")
        continue

    if(option == list_options[1]):
        os.system('clear')

        if(len(lista_compras) < 1 ):
            os.system('clear')
            print(lista_compras)
            print("Sua lista de compras está vazia!")
            continue


        print()
        try:
            refazer_lista = int(input("Informe uma das opções:\
                                       \n[1] Apagar um item especifico.\
                                       \n[2] Apagar toda a lista.\n=>").strip())
        except:
            print("Informe um valor válido.[1/2]!")
            continue

        if(refazer_lista == 1):
            os.system('clear')
            listar_item(lista_compras)
            print("Informe o Indice que deseja")
            try:
                indice_item = int(input("=> "))
                del lista_compras[indice_item]
                print("Item Apagado com sucesso!")
                '''if(lista_compras[indice_item]):
                    del lista_compras[indice_item]
                    print("Item Apagado com sucesso!")
                    continue'''
                continue

            except:
                print("Informe um indice existente valido.(ps: Apenas numeros)")
            

        elif(refazer_lista == 2):
            lista_compras.clear()
            print(lista_compras)
            print("Lista de compras Apagada com sucesso.")
            continue
        else:
            print("Opção inválida!")
            continue
        
    
    if(option == list_options[2]):

        if(len(lista_compras) < 1):
            os.system('clear')
            print(lista_compras)
            print("Sua lista de compras está vazia!")
            continue

        os.system('clear')
        print("Sua Lista de compras: ")
        listar_item(lista_compras)
        continue
    