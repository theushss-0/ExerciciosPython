"""  -- Criando arquivos com python -- 

# Usamos a função open para abrir um arquivo em python(ele pode ou não existir)

Modos:

r (read - leitura), w (write - escrita), x (para criação)
a (escrever ao final), b(binário)
t (modo texto), + (leitura e escrita)

Context manager - with (abre e fecha)
Métodos úteis:
-write, read (escrever algo, ler algo)
-writeline (escrever várias linhas)
-seek(mover o cursor)
-readline(Ler linha)
-readlines(ler linhas)

Vamos falar mais sobre o módulo OS, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o Módulo json, mas:
json.dump = Gera um arquivo json
json.load

"""


# Sobre os caminhos dos arquivos
caminho_relativo_arquivo = 'arquivoPastaAtual.txt'
caminho_completo_arquivo = '/home/matheus/Documentos/estudos-python/ExerciciosPython/arquivos/arquivoPastaAtual.txt'

#print(caminho_completo_arquivo)
#print(caminho_relativo_arquivo)


"""arquivo = open(caminho_completo_arquivo, 'w')

arquivo.write("Está funcionando")

arquivo.close()"""
from os import remove, unlink # apagam o arquivo (nos parâmetros deve ser informado o caminho e nome do arquivo)


#unlink(caminho_completo_arquivo) # descomentar e rodar o programa para apagar o arquivo

with open(caminho_completo_arquivo, "a+", encoding='utf8') as arquivo:
    print("Dados do arquivo:")
    arquivo.write("Linha\n")
    print()
    arquivo.seek(0,0)
    #print(arquivo.read())
    #print("\n\n")
    print(arquivo.readline().strip()) # readline() - Iterator (ler linha a linha conforme é chamada a função similar ao uso do next() em um __iter__)
    #print(arquivo.readline().strip())
    #print(arquivo.readline().strip())

    print()
    lista_linhas_arquivo = arquivo.readlines() # readlines() recebe os dados do arquivo a partir da ultima iteração (ex: se a ultima iteração foi na linha 2, ao usar a função é chamadado as proximas linhas para dentro de uma lista, no caso a partir da linha 3)
    print(lista_linhas_arquivo)
    print(lista_linhas_arquivo[0])

