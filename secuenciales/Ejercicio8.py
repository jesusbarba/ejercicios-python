# Programa: Ejercicio8.py
# Propósito: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber
# cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá
# en el mes tomando en cuenta su sueldo base y comisiones.
# Autor: Jesús Pablo Barba Reyes
# Fecha: 16/10/2022

# Petición de los datos
print('Sueldo base: ')
sueldo = float(input())
print('Primera Venta: ')
primera = float(input())
print('Segunda Venta: ')
segunda = float(input())
print('Tercera Venta')
tercera = float(input())

# Cálculo de los datos
primeraVentaTotal = float(primera / 10)
segundaVentaTotal = float(segunda / 10)
terceraVentaTotal = float(tercera / 10)

ventaTotal = primeraVentaTotal + segundaVentaTotal + terceraVentaTotal
sueldoFinal = sueldo + ventaTotal

# Impresión de los resultados por pantalla
print('La comisión de la primera venta es ', primeraVentaTotal, 'la de la segunda venta es ', segundaVentaTotal,
      'y de la tercera es ', terceraVentaTotal)
print('El total de las comisiones es ', ventaTotal, ', y el sueldo final es ', sueldoFinal)
