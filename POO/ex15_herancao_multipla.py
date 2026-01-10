#Problema do diamante em herança multipla

'''
Esse problema ocorre quando as duas classes herdadas, possuem um/mais métodos com a mesma assinatura,
por padrão a subclasse chama a primeira herdada(lado esquerdo)

para resolver o problema, é possível ver qual é a ordem das classes, da esqueda para direita, em uma lista ultimisando o metodo de classe mro()
'''


class A:

    def falar(self):
        print("Estou em A")


class B(A):
    
    def falar(self):
        print("Estou em B")

class C(A):


    def falar(self):
        print("Estou em C")

class D(B,C):
    ...


    def falar(self):
        print(D.mro()[1])
        super(D.mro()[1], self).falar()
    #def falar(self):
    #    print("Estou em D")



abc = D()
print(D.mro()) #B
abc.falar()