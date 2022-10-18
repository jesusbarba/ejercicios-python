# Programa: Ejercicio18.py
# Propósito: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca tu nombre completo y te mostraremos las iniciales')
print('------------------------------------------------------------')
print('Introduzca tu nombre: ')
nombre = str(input())
print('----------------------')
print('Introduzca el primer apellido: ')
primerApellido = str(input())
print('-------------------------------')
print('Introduzca el segundo apellido: ')
segundoApellido = str(input())
print('--------------------------------')

# Cálculo de los datos
nombreFinal = nombre[0]
primerApellidoFinal = primerApellido[0]
segundoApellidoFinal = segundoApellido[0]

nombreCompleto = nombreFinal + primerApellidoFinal + segundoApellidoFinal

# Impresión de los resultados por pantalla
print('Las iniciales de tu nombre completo son: ', nombreCompleto.upper())
