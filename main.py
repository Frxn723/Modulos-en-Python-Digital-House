print("Actividad 01 Modulos - random")
print() # El print() vacío se usa para generar un espacio en la consola.

import random

num1 = random.randint(1,10)
num2 = random.randint(11,20)
num3 = random.randint(21,30)
num4 = random.randint(31,40)
num5 = random.randint(41,50)


print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

suma = num1 + num2 + num3 + num4 + num5

print("La suma de los números generados es:", suma)

print()
print("Actividad 02 Modulos - datetime")
print()

import datetime

ahora = datetime.datetime.now()
print(ahora)

fecha = datetime.datetime(2006, 9, 16)
print(fecha)

diferencia = ahora - fecha
print(diferencia)

diferenciaEnDias = diferencia.days
print(diferenciaEnDias)

anios = diferenciaEnDias/365
print(anios)

print("tengo"+ " " + str(int(anios)) + " " + "años")