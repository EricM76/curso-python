# Evaluación de expresiones en Python.



# 1. Expresiones aritméticas
a = 7
b = 3

# 2. Expresión simple
resultado1 = a + b - 1  # Suma y resta en una sola expresión
# 8 - 9+ 6 --> -1 + 6
print(f"Resultado de a + b - 1: {resultado1}")

# 3. Expresión con paréntesis
resultado2 = (a + b) * 2  # Paréntesis cambian el orden de evaluación
print("Resultado de (a + b) * 2: " + str(resultado2))

# 4. Expresiones con operadores de comparación
mayor = a > b  # Verifica si a es mayor que b
igual = a == b  # Verifica si a es igual a b
print("a > b: " + str(mayor))
print(f"a == b: {igual}")

# 5. Expresiones booleanas
es_mayor_y_pos = (a > b) and (a > 0)  # Evaluación de dos condiciones con 'and'
print(f"Es a mayor que b y a es positivo?: {es_mayor_y_pos}")

# 6. Combinación de expresiones
expresion_compleja = (a + b) * (a - b) / 2  # Expresión con múltiples operaciones
print("Resultado de la expresión compleja: " + str(expresion_compleja))


# 2 + 5*(3-1)  --> 2 + 15 - 1 --> 17 - 1 --> 16