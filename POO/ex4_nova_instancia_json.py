from ex4_salvar_dados_json import Pessoa


listaDados = Pessoa.CarregarDadosJson()

pessoas = [ Pessoa(**pessoa) for pessoa in listaDados ]

'''
for pessoa in listaDados:
    pessoas.append(Pessoa(**pessoa))
'''



print(listaDados)
print()

#p1 = Pessoa('nomePessoa','sobrenomePessoa', 30,80,1.9)

#p2 = Pessoa('nomePessoa2','sobrenomePessoa2', 30,80,1.9)

#p1.SalvarJson(Pessoa.CarregarDadosJson())
#p2.SalvarJson(Pessoa.CarregarDadosJson())

print(pessoas[0].nome, pessoas[0].sobrenome, pessoas[0].idade)
print(pessoas[1].nome, pessoas[1].sobrenome, pessoas[1].idade)



