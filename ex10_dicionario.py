import os

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4'   
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'   
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções': ['4', '5', '3', '2'],
        'Resposta': '5'   
    }
]

opcao = ''
for pergunta in perguntas:

    for ch, vl in pergunta.items():

        if ch == 'Pergunta':
            print(ch,': ', vl)
            print()

        elif ch == 'Opções':

            for i, valor in enumerate(vl):
                print(i,') ', valor)

            opcao = input("Escolha a opção: ").strip()

            if vl[int(opcao)] == pergunta['Resposta']:
                os.system('clear')
                print("Acertou!! \n")
                continue
            else:
                os.system('clear')
                print("Errou!!\n")
                continue
