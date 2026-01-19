import calendar 
import locale


locale.setlocale(locale.LC_ALL, "") # pega a internacionalização conforme configurado no sistema operacional (LC_ALL - altera para todas as categorias)

print(calendar.calendar(2026))