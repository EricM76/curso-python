'''
Precedencia de operadores: El orden en que se evalúan los operadores en una expresión.
Asignación compuesta: Operadores como +=, -=, *=, /=, etc.
'''

# Operadores algebraicos en Python.

# 1. Definición de variables
x = 10
y = 4

# 2. Operadores básicos
suma = x + y  # Suma de dos números
resta = x - y  # Resta de dos números
multiplicacion = x * y  # Multiplicación de dos números
division = x / y  # División de dos números. Siempre devuelve un flotante
modulo = x % y  # Módulo (resto de la división)
potencia = x ** y  # Potencia, x elevado a la y
division_entera = x // y  # División entera, la parte entera de la división

# Imprimir resultados
print("Suma: " + str(suma))
print("Resta: " + str(resta))
print("Multiplicación: " + str(multiplicacion))
print(f"División: {division}")
print("Módulo: " + str(modulo))
print(f"Potencia: {potencia}")
print(f"División entera: {division_entera}")

x=9

x= x+ 1 
# 3. Asignación compuesta
x += 5  # Equivale a x = x + 5
print(f"x después de += 5: {x}")

y *= 2  # Equivale a y = y * 2
print(f"y después de *= 2: {y}")

# 4. Precedencia de operadores
# La precedencia determina el orden en que se evalúan los operadores
resultado = x + y * 2 - (10 / 5)  # Primero se multiplica y se divide, luego se suma y resta
print(f"Resultado de la expresión con precedencia: {resultado}")
