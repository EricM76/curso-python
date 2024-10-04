import os;
"""
Aquí vemos un ejemplo un poco más complejo que realiza el cálculo del promedio de tres notas:
"""
os.system('cls')
print("======================\nPROMEDIO DE TRES NOTAS\n======================\n")

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print()
print("El promedio de las tres notas es:",promedio)