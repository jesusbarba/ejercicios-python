# Programa: Ejercicio11.py
# Propósito: Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia,
# de modo que el resultado sea siempre positivo).
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Dime un primer número: ')
primero = float(input())
print('-----------------------')
print('Dime un segundo número: ')
segundo = float(input())
print('------------------------')

# Cálculo de los datos
distancia = abs(primero - segundo)

# Impresión de los resultados por pantalla
print('La distancia entre los 2 números es ', distancia)
