import os;

"""
Este ejemplo simple ilustra cómo se pueden utilizar las funciones input(), operadores aritmético y print() para escribir un 
programa simple que suma dos números proporcionados por el usuario:
"""

os.system('cls')
print("==================\nSUMA DE DOS NÚMEROS\n==================\n")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2

print("La suma de",numero1,"y",numero2,"es",suma)

