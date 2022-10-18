# Programa: Ejercicio13.py
# Propósito: Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene
# ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca un número para calcular su raíz cuadrada y cúbica: ')
numero = float(input())
print('--------------------------------------------------------------')

# Cálculo de los datos
cuadrada = pow(numero, 0.5)
cubico = pow(numero, 1/3)

# Impresión de los resultados por pantalla
print('La raíz cuadrada sería ', round(cuadrada, 2), ' y la raíz cúbica sería ', round(cubico, 2))
