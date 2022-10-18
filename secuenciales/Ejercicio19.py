# Programa: Ejercicio19.py
"""
Propósito:
Escribir un programa para calcular la nota final de un estudiante, considerando que:

    -cada respuesta correcta suma 5 puntos
    -cada respuesta incorrecta suma -1 puntos
    -cada respuesta en blanco suma 0 puntos.

Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes
tipos de respuestas puedan cambiar en el futuro?
"""
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Programa que nos calcula la nota del estudiante')
print('-----------------------------------------------')
print('Introduzca el número de respuestas correctas: ')
correctas = int(input())
print('----------------------------------------------')
print('Introduzca el número de respuestas incorrectas: ')
incorrectas = int(input())
print('------------------------------------------------')
print('Introduzca el número de respuestas en blanco: ')
blanco = int(input())
print('----------------------------------------------')

# Cálculo de los datos
notaEstudiante = (correctas * 5) - incorrectas
notaTotal = (correctas + incorrectas + blanco) * 5

notaFinal = (notaEstudiante * 10) / notaTotal

# Impresión de los resultados por pantalla
print('La nota que ha obtenido el estudiante es ', notaEstudiante, ' sobre ', notaTotal)
print('-------------------------------------------------------------------------------')
print('La nota normalizada del estudiante es ', notaFinal, ' sobre 10')
