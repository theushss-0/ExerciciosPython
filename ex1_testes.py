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

lista = [1,2,3 ,"Texto", {1,2,3}, ("Texto", "novo Texto"), 2.4,5.6, (3.4, 5.5)]


for item in lista:

    if isinstance(item, set):
        item.add(4)
        print(item)
        print()
    
    if isinstance(item, str):
        print(item.upper())
        print()

    if isinstance(item, (int, float)):
        print(item * 5)
        print()
import sys
## iterator
lista_iteravel= [1,2,3,4,5]
lista_iter = iter(lista_iteravel)
print(lista_iter.__next__())
print(lista_iter.__next__())
print(lista_iter.__next__())

## generator

list_valores = [n for n in range(10000)]

print("bites do tamanho da lista: ",sys.getsizeof(list_valores))

list_generator = (n for n in range(10000))
print("bites do primeiro valor do generetor: ",sys.getsizeof(list_generator))

print(list_generator.__next__())
print(list_generator.__next__())
print(list_generator.__next__())
print(list_generator.__next__())
"""


## Função Generator

def fnc_generator(n=0,maximun=10):
    while True:
        yield n

        n+=1
        if( n >= maximun):
            return "ACABOU"


##gen = fnc_generator(maximun=5)

'''
for value in gen:
    print(value)

gen = fnc_generator(maximun=5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def gen1():
    print("GEN1")
    yield 1
    yield 2
    yield 3
    print("Fim GEN1")

def gen2(gen=None):
    print("GEN2")
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print("Fim GEN2")

def gen3(gen):
    print("GEN3")
    yield from gen()
    yield 10
    yield 20
    yield 30
    print("Fim GEN3")

_gen1 = gen2(gen1())
_gen2 = gen2()
_gen3 = gen3(gen1)


for v in _gen1:
    print(v)
print()
for v in _gen2:
    print(v)
print()
for v in _gen3:
    print(v)
print()



try:
    a = 12
    b = 2

    print("Linha 1 ")
    x = a/b
    print("Linha 2 ")
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)

except (IndexError, TypeError) as e:
    print(e.__class__.__name__)
    print(e)
else:
    print("Não houveram erros")
finally:
    print("Finalisando try")

'''

'''

def concatenar(valor):
    valor_retorno = valor
    def a_concatenar(novo_valor):
        nonlocal valor_retorno
        valor_retorno += novo_valor
        return valor_retorno
    return a_concatenar


x = concatenar('a')
print(x("b"))
print(x("c"))
print(x("d"))

#funcao decoradora (cria a função e valida informação passada como parametro)
def cria_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        return resultado
    return interna

#sytaxe sugar - ao chamar a função "inverte_string", a mesma é passada como parâmetro para a função "cria_funcao"
@cria_funcao 
def inverte_string(string):
    return string[::-1]


# funcao que valida se o valor passado como parametro é uma string
def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Isso não é uma string!") # raise lança uma exceção (throws except type(info. lancada))
    

invertida = inverte_string("Luiz") # deixa o código mais limpo

print(invertida)
print(inverte_string("Matheus"))
print(inverte_string(123)) #TypeError - o valor precisa ser String
'''
'''
def decoradora(funcao):
    print("Função decoradora iniciada!")

    def interna(*args, **kwargs):
        print("aninhada!!")
        res = funcao(*args, **kwargs)
        return res

    return interna


@decoradora ## nesse momento a funcao decoradora já é iniciada, e fica aguando a execucao da funcao mais interna
def soma(x, y):
    return x+y

soma_xy = soma(1,2)

print(soma_xy)
'''
## Sobre Decoradores e Syntaxe Sugar
"""
def fabrica_decoradores(nome=None):
    def decorador(funcao):
        def interna(*args, **kwargs):
            res = funcao(*args, **kwargs)
            final = f"{res} {nome}"
            return final
        return interna
    return decorador



#ordem de baixo para cima
@fabrica_decoradores("5") # executa por ultimo
@fabrica_decoradores("4") # ...
@fabrica_decoradores("3") # ... 
@fabrica_decoradores("2") # executa segundo
@fabrica_decoradores("1") # executa primeiro
@fabrica_decoradores("Maria")
## sempre a funcao seguinte
def soma(x,y):
    return x + y 

def concatena_string(str1, str2):
    return str1 + str2


string_concatenada = concatena_string("Matheus","Henrique")
nums = soma(1,2)

print(string_concatenada)
print(nums)


"""
'''
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

produtos = [
    {'nomme': 'Produto 5', 'preco': 10.00}
]

'''



