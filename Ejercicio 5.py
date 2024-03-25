import os
os.system('clear')
"""Enunciado ejercicio 5
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a
dos decimales.
"""
print("¢¢¢ Banco Python ¢¢¢")
print()
Inversion = float(input("Ingrese la cantidad de dinero que desea depositar en su cuenta de ahorros: ¢ ")) # se toma el valor dado por el usuario para creaar la operación
Interes = 0.04 # dato base (quemado)
print()
print("El estado de los balances para los próximos 3 años serán:")
print()
Balance_1 = Inversion * (1 + Interes) # se guarda en la variable balance_1 el resultado del monto dado y se multiplica 1 más el interes quemado
print("El balance para el primer año será de: ¢" + str(round(Balance_1, 2)))  
Balance_2 = Balance_1 * (1 + Interes)  # se toma el resultado del primer balance_1 y se multiplica por 1 más el interes quemado
print("El balance para el segundo año será de: ¢" + str(round(Balance_2, 2)))
Balance_3 = Balance_2 * (1 + Interes)  # la variable balance_3 guarda el resultado de balance_2 y se multiplica por 1 más el interes quemado
print("El balance para el tercer año será de: ¢" + str(round(Balance_3, 2)))
print()
print("Gracias por ahorrar con nosotros")


