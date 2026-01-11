def calc_imc(pessoa_altura,pessoa_peso):
    imc = pessoa_peso / pessoa_altura**2
    return round(imc,3)


def classifica_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    

peso = float(input("Digite seu peso em kg: ").replace(',','.'))
altura = float(input("Digite sua altura em metros: ").replace(',','.'))

print(f"Seu IMC é: {calc_imc(altura,peso)}\nSua classigficação é \"{classifica_imc(calc_imc(altura,peso))}\"")