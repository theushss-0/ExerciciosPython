class MyCall:

    def __init__(self, numero):
        self.numero = numero


    def __call__(self, nome):
        print(f"{nome}, com numero {self.numero} está chamando!")
        return True
    

my_call = MyCall("1123456787")
my_call("Nome Pessoa")