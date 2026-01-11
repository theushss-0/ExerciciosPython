# funcao repr
def meu_repr(cls):
    class_name = cls.__class__.__name__
    class_dict = cls.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr

# funcao que adicionar repr
def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if "Terra" in resultado:
            print("Você está em casa!")

        return resultado
    return interno

@adiciona_repr #decorador para adicionar repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr #decorador para adicionar repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_planeta(self):
        return f"Este é o planeta {self.nome}!"


#Time = adiciona_repr(Time) # Adiciona repr a classe
flamengo = Time("Flamento")
cruzeiro = Time("Cruzeiro")

#Planeta = adiciona_repr(Planeta) # Adiciona repr a classe
jupiter = Planeta("Jupiter")
marte = Planeta("Marte")
terra = Planeta("Terra")


print(flamengo)
print(cruzeiro)

print(jupiter)
print(marte)

print(jupiter.falar_planeta())
print(terra.falar_planeta())