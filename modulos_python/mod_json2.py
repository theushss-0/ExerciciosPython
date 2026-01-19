import json
import os
from typing import TypedDict


class SenhorDosAneis(TypedDict):
   title: str
   original_title: str
   is_movie: bool
   imdb_rating: float
   year: int
   characters: list[str]
   budget: None


NOME_ARQUIVO = "testes/arquivo1.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

print(f"{os.path.dirname(__file__)}/testes/arquivo1.json")

print(CAMINHO_ABSOLUTO_ARQUIVO)

print(os.path.abspath(os.path.join(os.path.dirname(__file__),"arquivo1.json")))

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}'''

dict_filme: SenhorDosAneis = json.loads(string_json)

print(dict_filme)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as arquivo:
   json.dump(dict_filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
   filme_json:SenhorDosAneis = json.load(arquivo)
   print(filme_json)


print(filme_json["title"])
print(filme_json["year"])