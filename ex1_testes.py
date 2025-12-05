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