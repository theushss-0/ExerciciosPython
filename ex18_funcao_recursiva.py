#def recursiva(inicio=0, fim=10):
#    if inicio == fim:
#        return fim
#    inicio +=1
#    return recursiva(inicio, fim)



#print(recursiva())




def fatorial_n(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_n(n-1)
    

n = 5

print(fatorial_n(n))
