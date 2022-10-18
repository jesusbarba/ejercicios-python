# Programa: Ejercicio20.py
# Propósito: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos
# cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Programa que nos dice nuestro monedero actual')
print('---------------------------------------------')
print('Introduzca las monedas de 2 euros que tienes: ')
euros2 = int(input())
print('----------------------------------------------')
print('Introduzca las monedas de 1 euro que tienes: ')
euros1 = int(input())
print('---------------------------------------------')
print('Introduzca las monedas de 50 céntimos que tienes: ')
cent50 = int(input())
print('--------------------------------------------------')
print('Introduzca las monedas de 20 céntimos que tienes: ')
cent20 = int(input())
print('--------------------------------------------------')
print('Introduzca las monedas de 10 céntimos que tienes: ')
cent10 = int(input())
print('--------------------------------------------------')

# Cálculo de los datos
eurosTotal = (euros2 * 2) + euros1 + (cent50 / 2) + (cent20 / 5) + (cent10 / 10)

# Impresión de los resultados por pantalla
print('Nuestro monedero actual sería de ', round(eurosTotal, 2), ' euros')
