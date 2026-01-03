# Exercício - Lista de tarefas com desfazer e refazer

# indicação de leitura: o programador pragmático
# referencia: rubber duck debugging (debug com pato de borrachar)

# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['Fazer café'] -> adicionar 'fazer café'
# todo = ['Fazer café', 'caminhar'] -> Adicionar 'caminhar'
# desfazer = ['Fazer café'] -> Refazer ['Caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# comados: listar (listar tarefas), desfazer (desfazer info tarefa), refazer (refazer a tarefa)

import os, json

dir_arquivos = './arquivos/'
nome_arquivo= 'lista_tarefas.json'
CAMINHO_ARQUIVO = dir_arquivos + nome_arquivo

# lista com histórico das ultimas tarefas desfeitas
histLista = []

# lista de tarefas
tarefas = []

def desfazer():
    global tarefas, histLista 
    if not tarefas:
        print('A lista de tarefas está vazia!')
        return
    histLista.append(tarefas.pop())

def refazer():
    global tarefas, histLista
    if not histLista:
        print("Nenhuma tarefa a ser recuperada")
        return
    
    tarefas.append(histLista.pop())

        
def print_lista(listaTarefas):
    print("TAREFAS\n")
    for indice,item in enumerate(listaTarefas):
        print(f"{indice+1} - {item}")
    print()

def salvarDados(lista, caminho):
    tarefas = {
        'Tarefas': lista
    }
    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(
            tarefas,
            arquivo,
            indent=2
        )

def carregarDados(caminho):
    global tarefas

    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            aux_tarefas = list(*json.load(arquivo).values())
            if not aux_tarefas:
                return
            for item in aux_tarefas:
                tarefas.append(item)
    except:
        salvarDados([], caminho)
        return

#entrada = ''
comandos = 'listar', 'desfazer', 'refazer','salvar'
carregarDados(CAMINHO_ARQUIVO)

while True:
    
    print(f"\nComandos: {comandos[0]} - {comandos[1]} - {comandos[2]} - {comandos[3]}")
    print("Digite algum comando ou informar um item a listar")
    entrada = input("=>")


    if entrada == 'sair':
        os.system('clear')
        print('Até a proxíma!')
        break
    
    elif entrada == 'clear':
        os.system("clear")
    
    elif entrada in comandos:
        if entrada == 'listar':     
            if len(tarefas) <= 0:
                print('Nenhuma Tarefa na sua lista\n')
                continue
            os.system('clear')
            print_lista(tarefas)
            
        elif entrada == 'desfazer':
            desfazer()

        elif entrada == 'refazer':
            refazer()
        elif entrada == 'salvar':
            salvarDados(tarefas, CAMINHO_ARQUIVO)
    else:
        if len(entrada.strip()) <= 0:
            print("Nenhuma tarefa Informada!!")
            continue
        tarefas.append(entrada)
        print(f"Tarefa \"{entrada}\" adicionado a lista de tarefas!!\n")
    
