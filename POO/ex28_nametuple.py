from collections import namedtuple


carta = namedtuple("Carta", ["valor", "naipe"])
as_espada = carta("A", "Espada")
print(as_espada)

