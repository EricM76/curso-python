import os
""" 
OPERACIONES BÁSICAS

1. Crea un programa que solicite al usuario dos números enteros. 
2. Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
3. Muestra el resultado de cada operación en un formato claro y amigable. 

Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".
"""
os.system("cls")
print("================\nOPERACIONES BÁSICAS\n================")
numeroA = float(input("Ingrese un número: "))
numeroB = float(input("Ingrese un otro número: "))
resultado_suma = numeroA + numeroB
resultado_resta = numeroA - numeroB
resultado_multiplicacion = numeroA * numeroB
resultado_modulo = numeroA % numeroB
print("La suma de tus numeros es " + str(resultado_suma))
print("La resta de tus numeros es " + str(resultado_resta))
print("La multiplicación de tus numeros es " + str(resultado_multiplicacion))
print("El resto de tus numeros es " + str(resultado_modulo))
print()