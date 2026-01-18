# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz


from datetime import datetime
from pytz import timezone


datetime_ = datetime.now()
timestamp_ = datetime_.timestamp() # timestamp - quantidade de segundos desde 01-01-1970 até hoje
print("Timestamp: ", timestamp_)
print("DATA a partir do Timestamp: ",datetime_.fromtimestamp(timestamp_))
# pytz é um lib que pode pegar a data e hora atual em localidades diferentes
data_tz = datetime(2026,1, 17, 18,50, tzinfo=timezone('America/Atka')) # pytz é um lib que pode pegar a data e hora atual em localidades diferentes 
data_str = '2026-01-17 01:02:03'
data_str_format = '%Y-%m-%d %H:%M:%S'


#strptime() - é uma função que cria uma data com base na formação desejada
data = datetime.strptime(data_str, data_str_format)
print(data)
print(data_tz)
print(datetime.now(timezone('America/Atka')))