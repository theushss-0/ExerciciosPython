import requests #type: ignore
from bs4 import BeautifulSoup #type: ignore

url = "http://localhost:3333/"
response =  requests.get(url)
raw_html = response.text

parsed_html = BeautifulSoup(raw_html,'html.parser')

print(parsed_html.h1.text)