# type: ignore
import pandas as pd


df = pd.read_csv("../data/clientes.csv") # Ler o arquivo CSV

df.to_csv("clientes_aux.csv", index=False) # Salva o arquivo CSV

df.to_parquet("clientes.parquet", index=False) # gerar um arquivo com os dados criptografados

df_parquet = pd.read_parquet("clientes.parquet") # descriptografa o arquivo parquet e transforma em um dataframe

#print(df_parquet)


df.to_excel("clientes.xlsx", index=False) # criar um arquivo excel | necessário ter a biblioteca openpyxl instalada


df_xlsx = pd.read_excel("clientes.xlsx") # ler arquivos excel

#print(df_xlsx)

df_bobo = pd.read_csv("../data/bobo.csv", sep=";")

print(df_bobo)