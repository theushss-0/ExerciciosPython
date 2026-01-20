import string
import locale
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "testes/tamplate.txt"
locale.setlocale(locale.LC_ALL, "")

def converter_para_brl(numero:float)->str:
    brl = "R$ "+ locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2026,1,19)

dados = dict(
    nome='João',
    valor=converter_para_brl(1_234_567),
    data=data.strftime("%d/%m/%Y"),
    empresa='O. M.',
    telefone= "+55 (11) 7890-5432",
    remetente="Matheus"
)

class MyTemplate(string.Template):
    delimiter="%"

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    tamplate = MyTemplate(texto)
    print(tamplate.substitute(dados))


