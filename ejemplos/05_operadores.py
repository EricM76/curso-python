import os
""" 
======================
OPERADOR DE ASIGNACIÓN
======================
El operador de asignación = (igual) es muy importante en Python. Su función es diferente a la que habitualmente le damos en otros contextos, como la matemática. 
Se lo denomina “operador de asignación” y permite asignar un valor a una variable. Su función consiste en evaluar (resolver) la expresión que se encuentra a su derecha, y asignar el resultado a la variable de la izquierda.
"""
cantidad = 43       # int (enteros)
precio = 12.45      # float (reales)
nombre = "Adrián"   # string (cadenas)
encendido = True    # bool (lógicos

""" 
========================
EXPRESIONES Y SENTENCIAS
========================

Una expresión es una unidad de código que devuelve un valor y está formada por una combinación de operandos (variables y literales) y operadores.
Una sentencia o declaración define una acción. Puede contener alguna(s) expresiones. Son las instrucciones que componen el código de un programa y determinan su comportamiento. Finalizan con un Enter.
"""

a= 5
b= None
c = 10

resultado_suma = 5 + 2           # Suma del número 5 y el número 2
es_menor = a < 10          # Compara si el valor de la variable a es menor que 10
es_nulo = b is None       # Compara si la identidad de la variable b es None
resultado_operacion = 3 * (200 - c)   # Resta a 200 el valor de c y lo multiplica por 3

os.system('cls')
print("========================\nEXPRESIONES Y SENTENCIAS\n========================")
print("Resultado de la suma de 5 + 2 = " + str(resultado_suma))
print(str(b) + " ¿es nulo? = " + str(es_nulo))
print("Resultado de 3 * (200- " + str(c) + ") = " + str(resultado_operacion))
print()