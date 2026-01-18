from datetime import datetime

data_ = datetime.strptime("2001-12-16 12:45:30", "%Y-%m-%d %H:%M:%S")

ano_data = data_.strftime("%Y")#str - data_.year (int)
mes_data = data_.strftime("%m")#str - data_.month (int)
dia_data = data_.strftime("%d")#str - data_.day (int)

print(" | str\t| int  |")
print(" |------|------|")
print(f" | {ano_data}\t| {data_.year} |")
print(f" | {mes_data}\t| {data_.month}   |")
print(f" | {dia_data}\t| {data_.day}   |")

