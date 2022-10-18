# Programa: Ejercicio3.py
# Propósito: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Importamos el módulo
from math import sqrt

# Petición de los datos
print('Dime un valor para el cateto del triangulo rectángulo:')
primerCateto = float(input())
print('Dime un valor para el segundo cateto del triangulo rectángulo:')
segundoCateto = float(input())

# Cálculo de la hipotenusa
hipotenusa = sqrt(primerCateto**2 + segundoCateto**2)

# Impresión de los resultados por pantalla
print('La hipotenusa del triangulo rectángulo es ', hipotenusa)
