string = input("Informe alguma Palavra: ")
tamanho_string = len(string)
contador = 0
nova_string = "*"
#caractere_especial = "*"

while(contador<tamanho_string):

    nova_string += string[contador] + "*"
    contador+=1



print(nova_string)