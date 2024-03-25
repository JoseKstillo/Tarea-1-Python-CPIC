
import os
os.system('clear')

"""Enunciado ejercicio 6
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
final total.
"""
print(" Panadería Python. Siempre Fresca ")
print()
BarrasPan = int(input("Ingrese la cantidad de barras de pan vendidas que no son frescas: "))
PrecioBarra = 3.49 
Descuento = 0.6
CosteFinal = BarrasPan * PrecioBarra * (1 - Descuento) # la variable guarda el resultado de la cantidad dada por el usuario mutltiplicada por el precio
# por 1 menos el descuento base (valor quemado)
print()
print("El costo de una Barra de Pan Fresca es de: ¢" + str(PrecioBarra)) 
print("El descuento para una Barra de Pan no fresca es:" + str (Descuento * 100) + " %")
print("El costo final a pagar es de: ¢" + str (round(CosteFinal, 2)))
print()