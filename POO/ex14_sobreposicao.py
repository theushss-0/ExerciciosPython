

class A(str):
    atributo_a = "valor de A"

    def mostra_valor(self):
        print("A")

class B(A):
    atributo_b = "valor de B"

    def mostra_valor(self):
        print("B")

class C(B):
    atributo_c = "valor de C"

    def mostra_valor(self):
        super(C,self).mostra_valor()
        
        print("C")



abc = C()

#help(C)

abc.mostra_valor()
print(abc.atributo_a)
abc.mostra_valor()
print(abc.atributo_b)
abc.mostra_valor()
print(abc.atributo_c)


#class Foo:
#    ...



#help(Foo)

#print(C.mro())