# Programa: Ejercicio15.py
# Propósito: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
# intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca el valor de A: ')
a = float(input())
print('Introduzca el valor de B: ')
b = float(input())

# Cálculo de los datos
numero = b
b = a
a = numero

# Impresión de los resultados por pantalla
print('El valor de A sería ', a, ' y el valor de B sería ', b)
