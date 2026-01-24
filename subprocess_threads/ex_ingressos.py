from time import sleep
from threading import Thread
from threading import Lock

class Ingresso:
    def __init__(self,estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print(f"Estoque é insuficiente, estoque atual: {self.estoque}")
            self.lock.release()
            return self.estoque
        sleep(1)

        self.estoque-=quantidade
        print(f"Compra de {quantidade} realizada com sucesso, ainda temos {self.estoque} em estoque.")

        self.lock.release()
        return self.estoque
    
if __name__ == "__main__":

    ingressos = Ingresso(10)

    for i in range(1,20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    
    print(ingressos.estoque)
