class Camera:

    def __init__(self, modelo, filmando = False):
        self.modelo = modelo
        self.filmando = filmando

    
    def filmar(self):

        if self.filmando:
            print(f"{self.modelo} já está filmando")
            return
        
        print(f"{self.modelo} começou a filmar")
        self.filmando = True

    def fotografar(self):

        if self.filmando:
            print(f"Não pode Fotogravar, {self.modelo} está filmando!")
            return

        print(f"{self.modelo} tirou uma fotografia!")

    def parar_de_filmar(self):

        if not self.filmando:
            print(f"{self.modelo} não está filmando!")
            return
        
        print("Parando de Filmar")
        self.filmando = False



sony = Camera('Sony')
cannon = Camera('Cannon')

sony.filmar()
sony.filmar()
sony.fotografar()
sony.parar_de_filmar()
sony.fotografar()
print()
cannon.fotografar()
cannon.filmar()
cannon.fotografar()
cannon.filmar()
cannon.parar_de_filmar()
