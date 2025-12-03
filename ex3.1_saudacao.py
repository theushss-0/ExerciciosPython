
def saudacoes(hora_atual, nome):
    if (int(hora_atual[0]) >= 0 and int(hora_atual[0]) <= 11):
        print(f"Bom dia {nome}, agora são {hora_atual[0]} horas e {hora_atual[1]} minutos.")
    if (int(hora_atual[0]) >= 12 and int(hora_atual[0]) <= 17):
        print(f"Boa Tarde {nome}, agora são {hora_atual[0]} horas e {hora_atual[1]} minutos.")
    if (int(hora_atual[0]) >= 18 and int(hora_atual[0]) <= 23):
        print(f"Boa noite {nome}, agora são {hora_atual[0]} horas e {hora_atual[1]} minutos.")


while True:
    try:
        hora = input("Informe a hora atual(hh:mm): ")
        if (":" not in hora):
            print("O formato de hora precisa conter \":\"")
            continue
        if (not (len(hora) == 5)):
            print("O formato de hora pode está incorreto, verifique se preencheu todas as informações solicitadas!")
            continue
        valor_hora = hora.split(":")
        if (int(valor_hora[1]) >= 60 or  int(valor_hora[1]) < 0):
            print("Os minutos não podem ser maiores que 59 nem menores que 0")
            continue
        if (int(valor_hora[0]) > 23 or int(valor_hora[0]) < 0):
            print("A hora não pode ser maior ou igual a 24 nem menor que 0")
            continue
        nome = input("Qual o seu Nome: ")
        if(len(nome) < 5):
            print("Seu nome é muito Curto!")
            continue
        if(len(nome) <= 6):
            print("Seu nome é normal")
        elif(len(nome) > 6):
            print("Seu nome é muito Grande!")
            continue
    except:
        print("Ops! Algo deu errado")
        print("Certifique-se de informar no padrão estabelecido(hh:mm), ex: 01:30, 12:10 ...")
        continue
    break



saudacoes(valor_hora,nome)