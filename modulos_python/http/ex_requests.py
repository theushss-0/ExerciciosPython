# Requests para requisições HTTP
import requests #type:ignore

# http:// -> porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'

response = requests.get(url)
print(response.status_code)
print(response.headers) # cabeçalho da requisição
#print(response.content) # corpo do arquivo em bytecode
#print(response.json()) # quando for json
#print(response.text) # imprime o arquivo da resposta em texto
print(response)