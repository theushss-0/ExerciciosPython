#import os

#print(os.getenv("SENHA"))

from dotenv import load_dotenv #type: ignore
import os
load_dotenv()

#print(os.environ) // normalmente não é usado


os.environ["NOVAVARIAVEL"] = "Texto"

print(os.getenv('BD_PASSWORD'))

print(os.environ["BD_HOST"])

## PS: nunca enviar o .env para algum repositório remoto, manter apenas localmente, caso preciso algum exemplo, encaminhe sem as informações o .env-example