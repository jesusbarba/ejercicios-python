# Programa: Ejercicio14.py
# Propósito: Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca un número de dos cifras para que se le devuelva el número invertido: ')
numero = int(input())
print('--------------------------------------------------------------------------------')

# Cálculo de los datos
primerDigito = numero // 10
segundoDigito = numero % 10
primerDigitoTotal = str(segundoDigito)
segundoDigitoTotal = str(primerDigito)

# Impresión de los resultados por pantalla
print('El número invertido sería: ', primerDigitoTotal + segundoDigitoTotal)
