import os
""" 
CALCULADORA DE PROPINAS

Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante. 

El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
 
Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la propina). 
Finalmente, muestra los resultados en la pantalla.

"""
os.system("cls")
print("================\nCALCULADORA DE PROPINAS\n================")
monto = float(input("Ingrese el monto total de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de propina: "))
propina = (porcentaje * monto) / 100
total = monto + propina

print("Propina: " + str(propina))
print ("Total: " + str(monto + propina))

print()