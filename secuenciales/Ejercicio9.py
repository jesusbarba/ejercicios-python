# Programa: Ejercicio9.py
# Propósito: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá
# pagar finalmente por su compra.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Introduzca el total de la compra para realizarle el descuento: ')
compra = float(input())

# Cálculo de los datos
descuento = compra * 0.15
compraTotal = compra - descuento

# Impresión de los resultados por pantalla
print('El precio final de su compra es ', compraTotal)
