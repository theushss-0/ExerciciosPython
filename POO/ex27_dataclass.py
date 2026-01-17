from dataclasses import dataclass, asdict, astuple

@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nome_completo = f"{self.nome} {self.sobrenome}"

    #def __post_init__(self):
    #    self.nome_completo = f"{self.nome} {self.sobrenome}"


    #@property
    #def nome_completo(self):
    #   return f"{self.nome} {self.sobrenome}"

    #@nome_completo.setter
    #def nome_completo(self, valor):
    #   nome, *sobrenome =  valor.split()
    #   self.nome = nome
    #    self.sobrenome = " ".join(sobrenome)

if __name__ == "__main__":
    p1 = Pessoa("Matheus", "Henrique", 24)
    p2 = Pessoa("Matheus", "Henrique",24)
    #p1.nome_completo = "Matheus Henrique dos Santos Silva"
    #print(p1.nome_completo)
    #print(p1.sobrenome)
    print(asdict(p1))
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1))
    print(astuple(p1)[0])