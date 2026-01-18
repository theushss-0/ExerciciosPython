from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("16/12/2001 10:00:00", fmt)
data_final = datetime.strptime("17/01/2026 21:55:00", fmt)
delta = data_final - data_inicio
obj_delta = timedelta(days=10)


relative = relativedelta(data_final, data_inicio)
print(relative)
print(data_final + relativedelta(day=10))

daqui_dez_dias = data_final + obj_delta
print(daqui_dez_dias)

print(data_inicio > data_final)
print(data_inicio < data_final)
print(delta)
print(type(delta))
print(delta.days)
print(delta.seconds)
print(delta.max)
print(delta.min)
print(delta.microseconds)
print(delta.resolution)
print(delta.total_seconds()) # diferença total entre datas
