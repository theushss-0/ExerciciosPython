#import secrets
import string as s
from secrets import SystemRandom as Sr

#print(s.ascii_letters)
#print(s.digits)
#print(s.punctuation)

caracteres = s.ascii_letters + s.digits + s.punctuation
segredo = ''.join(Sr().sample(caracteres, k=15)) #choices

print()
print(segredo)


