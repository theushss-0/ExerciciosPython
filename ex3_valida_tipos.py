
num =0
try:
    num = int(input("Digite um numero Inteiro: "))
except:
    print("Ops! algo deu errado!")
    if (num is not int):
        print("Isso não é um numero inteiro")
    exit()


if (num % 2 == 0):
    print("O numero digitado é Par!")
else:
    print("O numero digitado é Impar!")
