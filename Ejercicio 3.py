import os
os.system('clear')

"""Enunciando ejercicio 3
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad por (interés dividido 100 más 1) elevado años
"""
print(" ¢¢¢ Calculadora de Inversión a Plazos ¢¢¢")
print()
Cantidad = float(input("Ingresa la Cantidad que desea Invertir: ¢ ")) # entrada de datos de usuario
Interes = float(input("Ingrese el Interes porcentual anual ? : % ")) 
años = int(input("¿A cuántos años?" )) 
print("El Capital Final obtenido será de:¢" + str(round(Cantidad * (Interes / 100 + 1) ** años, 2)))
# si no me equivoco el srt concatena, el round redondeará el resultado de la multipliación del interes dado por el usuario + 100 % + 1, multiplicado por la cantidad
#los signos ** validan los 2 decimales y int el numero entero de los años dados.
print("Felicidades, buena inversión.")