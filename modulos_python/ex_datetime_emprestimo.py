from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

vlr_emprestimo = 1_000_000
data_emprestimo = "20/12/2020"
num_meses = 12*5
tempo_pagamento = relativedelta(years=5)

vlr_parcela = round(vlr_emprestimo/num_meses, 4)

data_inicial = datetime.strptime(data_emprestimo, "%d/%m/%Y")
data_final =  data_inicial + tempo_pagamento

soma = 0
print("Ano/mês/dia inicial: ",data_inicial+relativedelta(months=+1))
print(f"VALOR TOTAL PAGO:{soma:,.2f}")
data_pagamento = data_inicial
print()
for parcela in range(1,num_meses+1, 1):
    soma += vlr_parcela
    data_pagamento += relativedelta(months=1)
    print(f"Parcela: {parcela} - {data_pagamento} - R$ {vlr_parcela:,.2f}")
    print(f"R$ {soma:,.2f} / R$ {vlr_emprestimo:,.2f}")

print()
print(f"VALOR TOTAL PAGO:{soma:,.2f}")

#print(num_meses)

print("Ano/mês/dia final: ",data_final)


#print(f"data: {data_pagamento} - R$ {vlr_pagamento}")

