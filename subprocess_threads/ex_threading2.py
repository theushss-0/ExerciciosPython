from threading import Thread
from time import sleep


def vai_demorar(texto,tempo):
    sleep(tempo) 
    print(texto)


t1 = Thread(target=vai_demorar, args=("Thread 1", 5))
t1.start() # start - inicia a thread em paralelo

#for i in range(10):
#    print(i)
#    sleep(1)

#while t1.is_alive(): # is_alive() - True enquanto a thead não termina a execução
#    print("Esperando a thread")
#    sleep(1)

t1.join() # join() - trava a execução do código nesse ponto, ao finalizar ele continua a execução a partir deste ponto

sleep(2)
x=5+2

print(x)