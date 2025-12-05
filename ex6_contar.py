frase = 'O Python é uma linguagem de programação'\
'multiparadigma'\
'Python foi criado por Guido Van Rossum'


i = 0 
letra = ['',0]
letra_mais_vezes = ['',0]
empate = []
qtd_empates = 0
qtd_vezes = 0
#passos = 1

while i < len(frase):
    #passos+=1
    letra_atual = frase[i]
    if(letra_atual == ' '):
        #passos+=1
        i+=1
        continue
    letra[0], letra[1] = letra_atual,frase.count(letra_atual)

    if(letra[1] > letra_mais_vezes[1] and letra_atual != ' ' ):
        #passos+=1
        letra_mais_vezes[0],letra_mais_vezes[1] = letra[0],letra[1] 
        qtd_vezes = letra_mais_vezes[1]
        if (empate):
            empate = []
        qtd_empates = 0

    elif(letra[1] == letra_mais_vezes[1] and letra[0] not in empate and letra[0] != letra_mais_vezes[0]):
        #passos+=1
        qtd_empates += 1

        empate.append(letra[0])
        empate.append(letra[1])
    i+=1

letras = []
todas_as_letras = []
todas_as_letras += empate + letra_mais_vezes
if(empate):
    #passos+=1
    print(f"Deu empate!")
    print(f"Empatados: {todas_as_letras}")
    print(f"Quantidade de empates: {qtd_empates}")
    for x in todas_as_letras:
        #passos+=1
        if type(x) is int:
            #passos+=1
            continue
        if x not in letras:
            #passos+=1
            letras.append(x)
    print(f"Letras: {letras}\nQuantidade de vezes: {qtd_vezes}")

else:
    #passos+=1
    print(letra_mais_vezes)
    print(f"A letra '{letra_mais_vezes[0]}' aparece {letra_mais_vezes[1]} vezes.")

#passos+=1
print()
print()
print("Quantidades de caracteres em 'frases': ",len(frase))
#print(f"Foram necessários {passos} passos para chegar a estes resultado.")
#print("Quantidades de passos menos as iterações no while por conta dos caracteres da frase: ",passos - len(frase))
