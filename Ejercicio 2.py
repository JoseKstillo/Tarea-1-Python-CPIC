import os
os.system('clear')

"""Enunciado ejercicio 2
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
respectivamente.
"""
print("Para realizar la siguiente división introduzca los valores solicitados.")
n = input("Introduce el dividendo (entero): ") # datos agregados por el usuario
m = input("introduce el divisor (entero): ") # datos agregados por el usuario
print(n + " entre " + m + " da un cociente de: " + str(int(n) // int(m)) + " y un resto de: " + str(int(n) % int(m))) #operación 
print("Gracias...")