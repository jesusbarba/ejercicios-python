# Programa: Ejercicio7.py
# Propósito: Realiza un programa que reciba una cantidad de minutos y muestre
# por pantalla a cuantas horas y minutos corresponde.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Dime una cantidad de minutos')
a = int(input())

# Cálculo de los datos
horas = int(a / 60)
minutos = int(a % 60)

# Impresión de los resultados por pantalla
print('Los minutos introducidos equivalen a ', horas, 'horas y ', minutos, 'minutos')
