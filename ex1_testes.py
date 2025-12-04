#from ex1_calc_imc import calc_imc, classifica_imc, init_program
# \r\n - CRLF (Carriage Return + Line Feed)
# \n   - LF (Line Feed)

# CRLF é usado em sistemas Windows para representar uma nova linha.
# LF é usado em sistemas Unix/Linux e macOS para representar uma nova linha.
print("teste\r\nteste")

# ESCAPE - caractere de escape 
print("teste \"OLA\" teste")

# r - raw string
print(r"teste \"OLA\" teste") # raw string - não interpreta caracteres de escape, usado para expressões regulares e caminhos de arquivos

#dentro de aspas simples é possível usar aspas duplas sem escape
print('testando "aspas" simples')

#init_program()

print("M" + "atheus")
"""
txt = input("teste: ")


hora = str(input("Informe a hora atual(hh:mm): "))
if (":" not in hora):
    print("O formato de hora precisa conter \":\"")
"""

'''
print()
contador = 0
while contador < 10:
    
    sair = input("Deseja sair? [s]im")
    sair = sair.lower()
    if (sair.startswith('s')):
        print("Tchau!!!")
        break
    contador+=1


'''
texto = "xtexto"

texto = texto[2].replace("x","m")

print(texto)


