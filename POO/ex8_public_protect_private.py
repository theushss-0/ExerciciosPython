# public, _protected, __private

# public - pode ser acessado fora da classe e em qualquer outro lugar(desde que respeite as regras do python quanto a objeto)
# _protected - não deve ser usado fora da classe pai ou de suas subclasses (usar metodos para isso - @property(getter) @nameProperty.setter(setter) )
# __private - não deve ser usado em lugar algum, que não seja dentro da classe onde a mesma foi criada

class Foo:
    def __init__(self):
        self.public = 'Isso é um atributo publico' 
        self._protected = 'Isso é um atributo protegido'
        self.__private = 'Isso é um atributo privado'

    def metodo_publico(self):
        return 'Isso é um método publico'
    
    def _metodo_protegido(self):
        return 'Isso é um método protegido'
    
    def __metodo_privado(self):
        return 'Isso é um método privado'
    

obj = Foo()

print(obj.public)
print(obj._protected) # funciona normalmente 'como se fosse um public', porém não é ATENÇÃO ao utilizar ou dar manutenção 
#print(obj.__private) ## dará erro - por padrão o __private faz um name mangling(desconfiguração de nomes), que desconfigura o nome do atributo ou metodo com dois underlines(__) no inicio do nome do atributo, mas ainda é possível acessar o mesmo utilizando "_Foo__private" 
#print(obj.__metodo_private()) ## dará erro

print(obj.metodo_publico()) 
print(obj._metodo_protegido()) # funciona normalmente 'como se fosse um public', porém não é ATENÇÃO ao utilizar ou dar manutenção 