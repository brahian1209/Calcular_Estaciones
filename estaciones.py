
from datetime import date, datetime
#mes = int (input("Digite el mes en el que se encuentra: "))
Y = int(input("Digite el año en el que se encuentra: "))

Y = 2022 # año bisiesto arbitrario, por si la fecha es un 29 de febrero
estaciones = [('invierno', date(Y,  1,  1),  date(Y,  3, 20)),
              ('primavera', date(Y,  3, 21),  date(Y,  6, 20)),
              ('verano', date(Y,  6, 21),  date(Y,  9, 22)),
              ('otoño', date(Y,  9, 23),  date(Y, 12, 20)),
              ('invierno', date(Y, 12, 21),  date(Y, 12, 31))]

def get_season(fecha):
    for estacion, inicio, fin in estaciones:
      if inicio <= fecha <= fin:
        return estacion

print (f'El Nivel de agua es: {Y} y este es optimo')
    