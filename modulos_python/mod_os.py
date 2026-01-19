import os


# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

print("a" * 50)
print("a" * 50)
print("a" * 50)
print("a" * 50)

os.system("clear")

os.system("echo \"Hello World\"")

os.system("ls ~ > ls_home.txt")


diretorio = os.path.join("/home/matheus/Documentos/estudos-python/ExerciciosPython/modulos_python","testes","teste.txt")
print(diretorio)

caminho, arquivo = os.path.split(diretorio)

print(caminho)
print(arquivo)

nome, extensao = os.path.splitext(arquivo)

caminho_mais_nome_arquivo, extensao = os.path.splitext(diretorio)

print(os.path.splitext(arquivo))

print(nome)
print(extensao)

print()

print(caminho_mais_nome_arquivo,extensao, sep="\n")

print(os.path.exists(diretorio))