from modulos import Calculos as calc

#CALCULADORA
def calculadora(x,y,op):
    match op.lower():
        case 'x':
            return calc.multiplicacao(x,y)
        case '/':
            return calc.divisao(x,y)
        case '+':
            return calc.soma(x,y)
        case '-':
            return calc.subtracao(x,y)

#TABUADA
def tabuada(num):
    print("--- T A B U A D A ---")
    for i in range(1,11,1):
        print(f"{num} x {i} = {num*i}\n")
    print("---------------------")


painel = """
-----------------------
 C A L C U L A D O R A
     T A B U A D A
      ( x / + - )
-----------------------
ps: Para iniciar clique
-----------------------
\'enter\':"""

opcoes = """
---------------------------------------
o que você quer fazer hoje?
1 - Tabuada
2 - Calculadora

ps: Digite apenas os numero da opção
---------------------------------------
R:"""

operacoes = """
-------------------------
escolha a operação
-------------------------
\'x\' - para Multiplicar
\'/\' - para Dividir
\'+\' - para Somar
\'-\' - para Subtrair
------------------------
=> """


while True:
    entrada = input(painel)
    if(not entrada):
        op = input(opcoes)
        if(op == '1'):
            num = int(input("Informe o numero que quer saber a tabuada\nN: "))
            tabuada(num)
        elif (op == '2'):
            escolha = input(operacoes).lower()
            escolha = escolha if escolha in ['x','/','+','-'] else "ERRO: DIGITE APENAS AS SEGUINTES OPÇÕES ['x','/','+','-']"

            if (not (len(escolha) == 1)):
                print(escolha)
                continue

            try:
                valor_x = float(input("Valor de X: "))
                valor_y = float(input("Valor de Y: "))
            except:
                print("Você precisa informar um numero!")
                continue
            
            resultado = calculadora(valor_x,valor_y,escolha)
            print()
            print(f"RESULTADO DA OPERAÇÃO: {valor_x} {escolha.upper()} {valor_y} = {resultado}")
            print()
        else:
            print("Informe uma opção Valida !!!")
            continue
    
    sair = input("Deseja sair? [S]im ")
    if(sair.lower() == 's'):

        print("Até uma Proxima vez !!!")
        break
    else:
        continue
    