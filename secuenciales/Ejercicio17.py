# Programa: Ejercicio17.py
# Propósito: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje
# hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca la hora de salida del ciclista: ')
horaSalida = int(input())
print('-------------------------------------------')
print('Introduzca los minutos de salida del ciclista: ')
minutoSalida = int(input())
print('-----------------------------------------------')
print('Introduzca los segundos de salida del ciclista: ')
segundoSalida = int(input())
print('------------------------------------------------')
print('Introduzca el tiempo que tardas en llegar a la ciudad B en segundos: ')
tiempoSegundos = int(input())
print('---------------------------------------------------------------------')

# Cálculo de los datos
tiempo = (horaSalida * 3600) + (minutoSalida * 60) + segundoSalida + tiempoSegundos

horaFinal = tiempo // 3600
minutoFinal = (tiempo % 3600) // 60
segundoFinal = (tiempo % 3600) % 60

# Impresión de los resultados por pantalla
print('Sales a las ', horaSalida, ' horas con ', minutoSalida, ' minutos y ', segundoSalida, ' segundos.')
print('-------------------------------------------------------------------------------------------------')
print('Llegas a las ', horaFinal, ' horas con ', minutoFinal, ' minutos y ', segundoFinal, ' segundos.')
