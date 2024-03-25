import os
os.system('clear')

"""Enunciado Ejercicio 4
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
así que deben calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
"""
PesoPayaso = 112
PesoMuñeca = 75
print(" Juguetería Python ")
print()
payasos = int(input("Ingrese la cantidad de Payasos a enviar: ")) # valor ingresado por el usuario
muñecas = int(input("Ingrese la cantidad de Muñecas a enviar: "))
print()
PesoTotal = PesoPayaso * payasos + PesoMuñeca + muñecas #mulptiplica el peso dado por la cantidad de ambos productos y los suma y muestra ese total
print("El peso total del paquete que será enviado es de : " + str(PesoTotal) , ("g"))
print()
print("Gracias por su compra...")

