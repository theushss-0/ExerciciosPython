import json
from typing import TypedDict


class SenhorDosAneis(TypedDict):
   title: str
   original_title: str
   is_movie: bool
   imdb_rating: float
   year: int
   characters: list[str]
   budget: None


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

senhor_dos_aneis: SenhorDosAneis = json.loads(string_json)


print(senhor_dos_aneis['title'])
print(senhor_dos_aneis['year'])
print(senhor_dos_aneis['characters'])


gerar_json = json.dumps(string_json)

print(gerar_json)

#with open('./testes/filme.json', "w", encoding='utf8') as arquivo:
#    json.dump(senhor_dos_aneis, arquivo, ensure_ascii=False, indent=2)