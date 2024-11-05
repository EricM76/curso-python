# Las variables almacenan datos que pueden ser usados y modificados más adelante.
# Python es dinámico, por lo que el tipo de dato se asigna automáticamente.

# Convenciones de nombres de variables:
# 1. Los nombres de variables deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
# 2. El resto del nombre puede contener letras, números y guiones bajos.
# 3. Los nombres de variables distinguen entre mayúsculas y minúsculas (case-sensitive). 
#    Por ejemplo, `edad` y `Edad` son variables diferentes.
# 4. Convención común: se utiliza snake_case para nombrar variables en Python (letras minúsculas separadas por guiones bajos).

# Ejemplos de nombres válidos:
nombre_completo = "Enzo Lisandro"  # Snake case (convención común en Python)
Edad = 14  # Nombre de variable válido (aunque es mejor usar minúsculas)
_peso = 60.5  # Los nombres de variables pueden empezar con guion bajo
numero_de_hijos = 2  # Snake case es más legible que escribir todo junto
PI = 3.14159  # Mayúsculas suelen utilizarse para constantes (aunque no es obligatorio)

# Ejemplos de nombres no válidos:
# 2nombre = "Juan"  # Inválido porque empieza con un número
# nombre-apellido = "Ana"  # Inválido porque contiene un guion (-) en lugar de un guion bajo (_)

# Asignación de variables:
edad = 25  # Una variable de tipo entero (int)
pi = 3.14159  # Una variable de tipo flotante (float)
nombre = "Ana"  # Una variable de tipo cadena (string)
es_estudiante = True  # Una variable booleana (True o False)

# Uso de las variables:
print("Edad:", edad)
print("PI:", pi)
print("Nombre:", nombre)
print("Es estudiante:", es_estudiante)

# También puedes reasignar valores a las variables:
edad = 26  # Reasignamos un nuevo valor a la variable edad
print("Nueva edad:", edad)

# Las variables pueden ser combinadas en operaciones:
area_circulo = pi * (10 ** 2)  # Usamos la variable pi para calcular el área de un círculo con radio 10
print("Área del círculo:", area_circulo)
