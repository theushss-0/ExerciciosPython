import os
import shutil
from pathlib import Path
from zipfile import ZipFile

#Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'testes/mod_dir_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / "testes/mod_dir_zip_compactado.zip"
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / "testes/mod_dir_zip_descompactado"

#Apaga os diretorios
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO,missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace(".zip", ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

#raise Exception

#Cria o diretorio deste exercicio
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


# Cria a pasta com os arquivos
def criar_arquivos(qtd:int, zip_dir:Path):
    for i in range(qtd):
        texto = 'arquivo_%d' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)

# criando a para mod_dir_zip com os arquivos
criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando um zip com os arquivos da pasta mod_dir_zip
with ZipFile(CAMINHO_COMPACTADO, "w") as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            #print(file)
            zip.write(os.path.join(root,file), file)

# imprindo o nome dos arquivos compactado 
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# extraindo os arquivos da pasta compactada
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)


