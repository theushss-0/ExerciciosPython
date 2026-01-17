# Gerar e validar CPFs
 
import re
import random
import os

# gera ultimos 2 digitos validos
def gerar_valido(nove_primeiros):

    cpf = ''
    contagem_regressiva = 10 if len(nove_primeiros) == 9 else 11 if len(nove_primeiros) == 10 else 0
    resultado =0

    for digito in nove_primeiros:
        resultado += int(digito) * contagem_regressiva
        contagem_regressiva-=1

    digito_aux = (resultado * 10) % 11 
    digito = digito_aux if digito_aux <= 9 else 0
    cpf = nove_primeiros + str(digito)

    return cpf

# gerar um CPF valido
def gerar_cpf():
    nove_digitos = ''
    for _ in range(9):
        nove_digitos += str(random.randint(0, 9))

    cpf_gerado = nove_digitos
    while len(cpf_gerado) < 11:
        cpf_gerado = gerar_valido(cpf_gerado)
     
    return cpf_gerado

# Verifica se o CPF é Válido
def verificar_cpf(cpf):
    cpf_formatada = valida_formatacao(cpf)

    if(not cpf_formatada[0]):
        return cpf_formatada[1]
        
    cpf_valido = cpf_formatada[-1][:9]
    while len(cpf_valido) < 11:
        cpf_valido = gerar_valido(cpf_valido)

    if cpf_formatada[-1] == cpf_valido:
        return f"CPF {cpf_formatada[-1]} é valido!"
    else:
        return f"CPF {cpf_formatada[-1]} é invalido!"

# Formata o CPF
def formatar_cpf(cpf):
    return re.sub(r'[^0-9]','', cpf)

# Valida formatação
def valida_formatacao(cpf):

    cpf = formatar_cpf(cpf)

    if len(cpf) != 11:
        mensagem = "Ops! quantidade de digitos errado"
        return False, mensagem,cpf

    valido = False if cpf[0] * len(cpf) == cpf else True 
    if (not valido):
        mensagem = f"CPF {cpf} é invalido!\nNumeros repetidos não são permitidos!"
        return False, mensagem,cpf
    
    mensagem = 'Sucesso'
    return True, mensagem, cpf



menu = """
---- GERAR E/OU VALIDAR CPF ----
1. Gerar
2. Validar
3. Sair
=>"""

while True:

    try:
        opcao = int(input(menu))
    except:
        os.system('clear')
        print("Informe uma opção valida(1,2 ou 3)!")
        continue

    if(opcao == 3):
        print("Até uma proxima vez!")
        break

    elif(opcao == 1):
        os.system('clear')
        while True:
            try:
                quantidade = int(input("Quantos CPFs deseja gerar?\n=>"))
            except:
                print("Informe apenas numeros!")
                continue
            for i in range(quantidade):
                print(f"CPF({i+1}): {gerar_cpf()}")
            continuar = str(input("\nDeseja continuar? (S/N)")).strip().upper()
            if(continuar == 'S'):
                os.system('clear')
                continue
            else:
                os.system('clear')
                break
    elif(opcao == 2):
        os.system('clear')
        while True:
            cpf_informado = str(input("Informe o CPF que deseja validar: "))
            print(verificar_cpf(cpf_informado))

            continuar = str(input("\nDeseja validar outro CPF? (S/N)")).strip().upper()
            if(continuar == 'S'):
                os.system('clear')
                continue
            else:
                break

    else:
        os.system('clear')
        print("Opção Invalida, tente novamente!")
