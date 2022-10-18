# Programa: Ejercicio10.py
""" Propósito:
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los
siguientes porcentajes:
- 55% del promedio de sus tres calificaciones parciales.

- 30% de la calificación del examen final.

- 15% de la calificación de un trabajo final.
"""
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Calificaciones finales de la materia Algoritmos')
print('-----------------------------------------------')
print('Introduzca la nota del primer parcial')
primerParcial = float(input())
print('Introduzca la nota del segundo parcial')
segundoParcial = float(input())
print('Introduzca la nota del tercer parcial')
tercerParcial = float(input())
print('Introduzca la nota del examen final')
examen = float(input())
print('Introduzca la nota del trabajo final')
trabajo = float(input())

# Cálculo de los datos
parciales = ((primerParcial + segundoParcial + tercerParcial) / 3) * 0.55
examenFinal = examen * 0.3
trabajoFinal = trabajo * 0.15
notaFinal = round(parciales + examenFinal + trabajoFinal, 2)

# Impresión de los resultados por pantalla
print('La nota final de la asignatura Algoritmos es: ', notaFinal)
