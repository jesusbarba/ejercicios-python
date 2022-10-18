# Programa: Ejercicio16.py
"""
Propósito:
    Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
    El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre
    los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
    alcanzará el vehículo más rápido al otro.
"""
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca la distancia entre los dos coches: ')
distancia = float(input())
print('----------------------------------------------')
print('Introduzca la velocidad del primer coche: ')
velocidadPrimerCoche = float(input())
print('------------------------------------------')
print('Introduzca la velocidad (más rápida) del segundo coche: ')
velocidadSegundoCoche = float(input())
print('-------------------------------------------')

# Cálculo de los datos
tiempo = 60 * distancia / (velocidadSegundoCoche - velocidadPrimerCoche)

# Impresión de los resultados por pantalla
print('El coche mas rápido alcanzará al otro coche en ', tiempo, ' minutos')
