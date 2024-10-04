""" 
======================
OPERADORES ARITMÉTICOS
======================

Realizan las operaciones aritméticas comunes. Requieren uno o dos operandos (operadores unarios o binarios). Se aplican las reglas de precedencia propias del álgebra:
"""
print("======================\nOPERADORES ARITMÉTICOS\n======================\n")

suma = 12 + 5
print("SUMA: suma dos operandos.")
print(suma) # 17
print()

print("RESTA: resta al operando de la izquierda el valor del operando de la derecha. Utilizado sobre un único operando, le cambia el signo.")
resta = 23 - 4
print(resta) # 19
numero = -32
print(numero) # -32
print()

print("MULTIPLICACION: Producto de dos operandos.")
multiplicacion = 5 * 8
print(multiplicacion) # 40
print()

print("DIVISIÓN: Divide el operando de la izquierda por el de la derecha (el resultado siempre es un float).")
division = 8 / 2
print(division) # 4.0
division2 = 14 / 5
print(division2) # 2.8
print()

print("OPERADOR MÓDULO: Obtiene el resto de dividir el operando de la izquierda por el de la derecha. uno de sus usos es para saber si un número es par o impar")
modulo = 8 % 2
print(modulo) # 0 (8 es par)
modulo = 9 % 2
print(modulo) # 1 (9 es impar)
print()

print("DIVISIÓN ENTERA: Obtiene el cociente entero de dividir el operando de la izquierda por el de la derecha.")
divEntera = 10 // 6
divEntera2 = 25 // 4
print(divEntera) # 1
print(divEntera2) # 6
print()

print("POTENCIA: El resultado es el operando de la izquierda elevado a la potencia del operando de la derecha.")
potencia = 2 ** 3
potencia2 = 10 ** 2
print(potencia) # 8
print(potencia2) # 100
print()

print("RAIZ CUADRADA: ara la raíz cuadrada Python no tiene operador aritmético en particular, pero podemos utilizar ** con un exponente de 0.5 (para raíz cuadrada) o fracción (para raíz cuadrada u otras raíces).")
raiz = 9 ** 0.5
print(raiz) # 3.0
raiz = 9 ** (1/2)
print(raiz) # 3.0
raiz = 125 ** (1/3)
print(raiz) # 5.0