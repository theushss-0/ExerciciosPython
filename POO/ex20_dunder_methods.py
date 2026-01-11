class Ponto:
    def __init__(self, x, y, z="String"):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    
    # __str__  -- serve para mostrar alguma coisa especifica da classe para visualização(ela é chamada primeiro por padrão)
    def __str__(self):
        return f"valores de x e y: ({self.x}, {self.y})"
       
    #caso não houver o __str__, ela procura a __repr__    
    # __repr__ -- serve para mostrar uma representação da classe (mais util para devs)
    def __repr__(self):
        #nome_classe = self.__class__.__name__
        nome_classe = type(self).__name__
        return f"{nome_classe}(x = {self.x!r}, y = {self.y!r}), z={self.z!r}" # Usar !r para representar de forma mais compreensiva o tipo de dado
    
    def __add__(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Ponto(result_x, result_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other

if __name__ == "__main__":
    
    p1 = Ponto(12, 15)
    p2 = Ponto(23,3)
    p3 = p1 + p2 # __add__

    print("p3 => ", p3)
    print(f"p1 é maior que p2 ?", p1 > p2) # __gt__
    print(f"p1 é menor que p2 ?", p2 > p1) # __gt__


    print()
    # Caso __repr__ e __str__ não estiverem definidas na classe, é exibido o tipo e endereço na memória da classe
    print(p1)   
    print(repr(p1)) # exibindo: Ponto(x = 12, y = 15)
    print(str(p1))
    print(f"{p1!r}")