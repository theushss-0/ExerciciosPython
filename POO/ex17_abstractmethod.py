from abc import ABC, abstractmethod


class AbstractFoo:


    def __init__(self, nome):
        self._nome = None
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    @abstractmethod
    def nome(self, nome): ...

class Foo(AbstractFoo):

    #nome = ''

    def __init__(self, nome):
        super().__init__(nome)

    @AbstractFoo.nome.setter
    def nome(self, nome):
        self._nome = nome


foo = Foo("Bar")

print(foo.nome)