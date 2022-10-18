# Programa: Ejercicio2.py
# Propósito: Calcular el perímetro y área de un rectángulo dada su base y su altura.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Dime un valor para la base del rectángulo:')
b = float(input())
print('Dime un valor para la altura del rectángulo:')
h = float(input())

# Cálculo del área y del perímetro
Area = b*h
perimetro = 2*h + 2*b

# Impresión de los resultados por pantalla
print('El area del rectángulo es', Area, 'y su perimetro es', perimetro)
