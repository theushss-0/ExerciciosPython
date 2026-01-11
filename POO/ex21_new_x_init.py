class A:
    def __new__(cls, *args, **kwargs):
        print("Antes de iniciar o __init__")
        instancia = super().__new__(cls)
        print("depois de iniciar o __init__")
        return instancia


    def __init__(self, x):
        self.x = x
        #print(self, self.x)

    def __repr__(self):
        return "A()"
    

#a = A()

a = A(123)
print(a.x)