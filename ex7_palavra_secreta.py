import os
print("ATÉNÇÃO: \"Isso é para o ADM da vez!!!\"\n")
genero = input("Qual o genero dessa deseja?\n=>")
palavra_secreta = input("Qual é a palavra Secreta dessa rodada?\n=>")
numLetras = len(palavra_secreta)
numTentativas = 0
aux_palavra = str("*," * numLetras)[:-1]
os.system('clear')

desistir = False
aux = aux_palavra.split(",")

while not desistir:
    print(f"Genero: {genero}")
    print("=======================================")
    if aux_palavra.strip() == palavra_secreta:
        break

    letra = str(input("Digite uma letra: "))
    numTentativas+=1

    if (len(letra) > 1):
        os.system('clear')
        print("Digite apenas uma letra!\n")
        continue
    
    if (letra in palavra_secreta):
        #print("\ntamanho palavra_secreta: ", len(palavra_secreta))



        for i in range(numLetras):
            if palavra_secreta[i] == letra:
                aux[i] = letra
                aux_palavra = "".join(aux)

        #print(aux)  
        os.system('clear')
        print("Palavra: ",aux_palavra)
        print("Você acertou uma letra.")
        continue
    else:
        os.system('clear')
        print("\nPalavra: ",aux_palavra)
        print("Que pena você errou, tente outra letra!")

    desistir = True if input("Deseja continuar tentando? (S/N)\nR: ").lower()  == 'n' else False
    print("=======================================")

os.system('clear')
if(aux_palavra == palavra_secreta):
    print(f"Parabéns!!! Você conseguiu acertar a palavra.\nPalavra Correta: \"{palavra_secreta}\"\n")
    print(f"Você acertou com {numTentativas} tentativas.")
else:
    print(f"Que pena! Você não acertou, a palavra correta era \"{palavra_secreta}\"!\n")
    print(f"Seus acertos: {aux_palavra}")
    print(f"Quantidade de tentativas: {numTentativas}")