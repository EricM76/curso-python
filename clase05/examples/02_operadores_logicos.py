# Operadores lógicos en Python

# Los operadores lógicos son `and`, `or` y `not`.

# ✅ `and` devuelve True si ambos operandos son True
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia  # True

# ✅ `or` devuelve True si al menos una condición es True
es_adolescente = edad >= 13 or edad <= 19  # False

# ✅ `not` invierte el valor lógico de una expresión
es_menor = not edad >= 18  # False

# Ejemplo práctico: comprobando varias condiciones
es_adulto = edad >= 18 and not es_adolescente  # True


# Retornan un  valor bool

# AND
True or False # False
True and True # True

False or True

False and False

# ✅ `and` devuelve True si ambos operandos son True
edad = 15
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia # 15 >= 18 and True
# True and True

print("Puede: ", puede_conducir)


not True


