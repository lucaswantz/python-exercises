import datetime as dt
import time as tm

#time retorna o tempo atual em segundos desde o Epoch. (1 de janeiro de 1970)
tm.time()

#conversão para data e hora
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

#Atributos úteis de data e hora:
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second 
# obter ano, mês, dia, etc

#timedelta é uma duração que expressa a diferença entre duas datas.
delta = dt.timedelta(days = 100) # cria um delta de 100 dias
delta

#date.today retorna a data local atual.
today = dt.date.today()

today - delta # a data 100 dias atrás

today > today-delta # comparar datas
