from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    
    def run(self):
        sleep(self.tempo)
        print(self.texto)



obj_thread1 = MyThread("Thread 1", 5)
obj_thread1.start() ## executa a thread em paralelo run()

obj_thread2 = MyThread("Thread 2", 3)
obj_thread2.start() ## executa a thread em paralelo run()

obj_thread3 = MyThread("Thread 3", 2)
obj_thread3.start() ## executa a thread em paralelo run()


for i in range(10):
    print(i)
    sleep(1)