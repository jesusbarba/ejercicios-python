# Programa: Ejercicio12.py
# Propósito: Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano.
# Calcula y muestra la distancia entre ellos.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# importamos el módulo
import math

# Petición de los datos
print('Distancia entre coordenadas ')
print('----------------------------')
print('Introduce la coordenada x1: ')
x1 = int(input())
print('Introduce la coordenada y1: ')
y1 = int(input())
print('Introduce la coordenada x2: ')
x2 = int(input())
print('Introduce la coordenada y2: ')
y2 = int(input())

# Cálculo de los datos
distancia = int(abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))

# Impresión de los resultados por pantalla
print('La distancia que hay entre ellos es ', distancia)
