nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if(not nome or not idade):
    print("Ops, campos vazios!")
    exit()


print(f"Seu nome é {nome} !")
print(f"Seu nome invertido é {nome[::-1]}!")

if (" " in nome):
    print("Seu nome contém espaços!")
    
else:
    print("Seu nome não contém espaços!")

print(f"Seu nome tem {len(nome)} letras")

print(f"A primeria letra do seu nome é {nome[0]}")
print(f"A ultima letra do seu nome é {nome[-1]}")

