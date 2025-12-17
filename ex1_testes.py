#from ex1_calc_imc import calc_imc, classifica_imc, init_program
# \r\n - CRLF (Carriage Return + Line Feed)
# \n   - LF (Line Feed)

# CRLF é usado em sistemas Windows para representar uma nova linha.
# LF é usado em sistemas Unix/Linux e macOS para representar uma nova linha.
#print("teste\r\nteste")

# ESCAPE - caractere de escape 
#print("teste \"OLA\" teste")

# r - raw string
#print(r"teste \"OLA\" teste") # raw string - não interpreta caracteres de escape, usado para expressões regulares e caminhos de arquivos

#dentro de aspas simples é possível usar aspas duplas sem escape
#print('testando "aspas" simples')

#init_program()

#print("M" + "atheus")
"""
txt = input("teste: ")


hora = str(input("Informe a hora atual(hh:mm): "))
if (":" not in hora):
    print("O formato de hora precisa conter \":\"")
"""

'''
print()
contador = 0
while contador < 10:
    
    sair = input("Deseja sair? [s]im")
    sair = sair.lower()
    if (sair.startswith('s')):
        print("Tchau!!!")
        break
    contador+=1


'''
#texto = "xtexto"

#texto = texto[2].replace("x","m")

#print(texto)
'''
lista_a = ['texto', 'texto2']
lista_b = lista_a.copy()

lista_a[0] = 'textoNovo'

print(lista_b)

var_a = "texto"
var_b = var_a

var_a = "novotexto"
print(var_b)


lista = ['Maria', 'José', 'Matheus']
lista.append('José')
lista.append(10)
lista.append(True)
lista.append(3.14)


indices = range(len(lista))

for indice in indices:
    print(indice, " - ", lista[indice], type(lista[indice]))


_,__,nome, nome2, *resto = ['Matheus',"José","MaisNomes", "NovoNome"] # *Caractere, o Asterisco seguido de algum caractere ou conjunto
                                                                 # de caracteres, cria uma lista que armazena novos valores da atribuição

   
print()
print(_,__,nome, nome2, resto)
    

nova_lista = ['teste', 'teste1', 'teste2']

nova_lista_enumerada = enumerate(nova_lista)
nova_lista_enumerada2 = enumerate(nova_lista)
#range_nova_lista = range(nova_lista_enumerada2)

print(nova_lista_enumerada)
for item in nova_lista_enumerada:
    indice, valor = item
    print(indice, valor)

print()

for item in enumerate(nova_lista):
    indice, valor = item
    print(indice, valor)

print()

for indice,valor in enumerate(nova_lista):
    print(indice, valor, nova_lista[indice])

print()
for item in nova_lista_enumerada:
    indice, valor = item
    print(indice,valor)

range_nova_lista = range(len(nova_lista))
for i in range_nova_lista:
    print(next(nova_lista_enumerada2))

try:
    print(next(nova_lista_enumerada2)) ## erro devido não existir um proximo valor no iterator
except:
    print()


    
# COMO RESOLVER A IMPRECISÃO DE TIPOS FLUTUANTE
import decimal # biblioteca que faz a correção

num_float1 = decimal.Decimal('0.1')# Utilizando uma classe da biblioteca decimal
num_float2 = decimal.Decimal('0.7')
num_impreciso = num_float1 + num_float2 
print(f"{num_impreciso:.2f}") # uma das forma é forçando que ele ajuste as casas decimais fazendo assim o arredonamento
print(round(num_impreciso,3)) # outra forma é utilizando a função round, que faz o mesmo que o caso acima, porém o retorno é o numero flutuante
print(num_impreciso) # soma dos dois valores após usar a classe Decimal da biblioteca

'''
"""

string = 'ABC'
lista = ["Maçã", "Banana", "Pêra"]
tupla = 'Matheus', 'Henrique','dos','Santos', 'Silva'
lista_de_lista = [['Henrique','Santos'], 'silva',['josé', ['josé']]]
a,b,*_,c = tupla

print(*tupla, sep="\n")
print()
print(*lista, sep="--")
print(*string)
print()
print(*lista_de_lista, sep='\n')

print("jorge", lista, sep=string, end=' ')

print()
print()

print(a,b,c, sep='-')
print(*_,sep='\n')



pessoas = {
    "nome": "Jorge",
    "idade": 30
}

dados_novos = {
    "sobrenome": "Oliveira",
    "nascimento": 1898,
}

dd_pessoa01 = pessoas
print(dd_pessoa01)

nome, idade = pessoas.values()
print(nome, idade)

pessoa_nome, pessoa_idade = pessoas.items()
print(pessoa_nome, pessoa_idade)


(ch_nome, nome),(ch_idade, idade) = pessoas.items()
print(ch_nome,nome,'\n', ch_idade, idade)

infos_pessoa = {**pessoas, "comidas-favorita": 'lasanha', **dados_novos}
infos_pessoa.update({'time':"Flamento", 'cpf': 123456789})
print("Dados da pessoa: ", infos_pessoa)

lista = [numero * 2 for numero in range(10)]
lista_range = list(range(10))
lista_for = []
for numero in range(10):
    lista_for.append(numero*3)

print(lista)

print(lista_range)

print(lista_for)
"""

from decimal import Decimal

tab_precos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30},
]

print(tab_precos)


tab_precos_atualizados = [
    {**produto,"preco": produto['preco']*1.05 }
    if produto["preco"] > 20 else {**produto} 
    for produto in tab_precos
    if produto['nome'] == 'p3'
]

print(*tab_precos_atualizados, sep='\n')