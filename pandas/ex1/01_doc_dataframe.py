import pandas as pd
import os

# Limpa o terminal
def clear_terminal():
    os.system('clear')



df = pd.DataFrame(
    {
        "name": [
            "Matheus",
            "José",
            "Maria"
        ],
        "age": [23, 45, 37],
        "sex": ['Male', "Male", "Female"]
    }
)

print(df)

print(type(df))

print("\nNames:")
print(df.name)
print("\nAges:")
print(df.age)
print("\nSex:")
print(df.sex)
#clear_terminal() # descomente para limpar o terminal caso já tenha testado
exit()

print(df["name"])
print(df["age"])
print(df["sex"])

#clear_terminal() # descomente para limpar o terminal caso já tenha testado
#exit()

print(df.iloc[0])
print()
print(df.iloc[-1])

#clear_terminal() # descomente para limpar o terminal caso já tenha testado
#exit()

# maior idade

print(df.age.max())

# menor idade
print(df.age.min())


#clear_terminal() # descomente para limpar o terminal caso já tenha testado
#exit()
media = sum(df['age']) / len(df['age'])
print("Media de idades: ", media)
print("(DF) Media de idades: ", df["age"].mean())
print("(DF) Variancia entre as idades: ",df['age'].var())


#clear_terminal() # descomente para limpar o terminal caso já tenha testado
#exit()
print()
print(df.describe())


#clear_terminal() # descomente para limpar o terminal caso já tenha testado
#exit()



