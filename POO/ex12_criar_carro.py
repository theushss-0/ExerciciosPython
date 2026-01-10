# Exercicio com classes
# 1- Crie uma classe Carro (nome)
# 2- Crie uma classe Motor (nome)
# 3- Crie uma classe Fabricante(nome)
# 4- Faça a ligação entre Carro tem motor
# obs.: Um motor pode ser de vários carros
# 5- Faça a ligação entre Carro e Fabricante
# Obs.:Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricantes na tela 

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    

    def listar_info_carro(self):
        print()
        print("Carro: ", self.nome)
        print("Motor: ", self.motor.nome)
        print("Fabricante: ", self.fabricante.nome)
        print()
    
    def __del__(self):
        print("APAGANDO, ", self.nome)


class Motor:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        print("APAGANDO, ", self.nome)

class Fabricante:
    def __init__(self,nome):
        self.nome = nome
        self.carros = []

    def inserir_carros(self, *carros):
        self.carros.extend(carros)

    def listar_carros(self):
        print()
        print(self.nome)
        for carro in self.carros:
            print('Nome: ',carro.nome)
            print('Motor: ',carro.motor.nome) 

    def __del__(self):
        print("APAGANDO, ", self.nome)

        


carro1 = Carro('Fiat')
motor1 = Motor('Motor A')
fabricanteA = Fabricante("Fabricante A")

carro1.motor = motor1
carro1.fabricante = fabricanteA

#fabricanteA.inserir_carros(carro1)



#fabricanteA.listar_carros()
print()
carro1.listar_info_carro()
print()

