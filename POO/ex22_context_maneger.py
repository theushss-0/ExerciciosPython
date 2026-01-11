from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print("Criando arquivo")
        arquivo = open(caminho, modo, encoding="utf8")
        yield arquivo
    except Exception as error:
        print("Aconteceu um erro")
        print("Error: ", error)
    finally:
        print("fechando arquivo")
        arquivo.close

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        print("INIT")
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    
    def __enter__(self):
        print("ENTER")
        self._arquivo = open(self.caminho_arquivo, self.modo)
        return self._arquivo
    

    def __exit__(self, class_exeption, exception_, traceback_):
        print("EXIT")
        self._arquivo.close()

        #print(*exception_)
        #raise class_exeption(*exception_.args).com_excecao(traceback_)

        exception_.add_note("Minha nota sobre o erro")
        print(class_exeption)
        print(exception_)
        print(traceback_)
        
    

"""
with MyOpen("../arquivos/MyOpen.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n", 123) #Error
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
"""

with my_open("../arquivos/FuncMyOpen.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n", 123)
    arquivo.write("Linha 4\n")
