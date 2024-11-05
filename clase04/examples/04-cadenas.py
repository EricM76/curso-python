# Cadenas en Python
# ⭐ https://docs.python.org/es/3/library/stdtypes.html#string-methods
# ⭐ https://ellibrodepython.com/cadenas-python

# Definición básica: Una cadena es una secuencia inmutable de caracteres, es decir, no puede ser modificada una vez creada.
# Se puede usar comillas simples ' ' o dobles " " para definir una cadena.

#         012345678910
cadena = "Hola, Mundo"

"Hola"

# Acceso a caracteres individuales de una cadena
# Se accede a los caracteres usando índices. Los índices comienzan desde 0.
# El índice negativo cuenta desde el final hacia el principio (-1 es el último carácter).
primer_caracter = cadena[0]  # "H"
ultimo_caracter = cadena[-1]  # "o"

# Concatenación de cadenas
# Puedes usar el operador + para unir dos o más cadenas.
saludo = "Hola"
nombre = "Mundo"
frase = saludo + ", " + nombre  # "Hola, Mundo"

# También se puede concatenar usando f-strings (Python 3.6+), lo que facilita la inserción de variables.
frase_fstring = f"{saludo}, {nombre}"  # "Hola, Mundo"

# Longitud de una cadena (cantidad de caracteres)
# La función len() devuelve el número de caracteres en la cadena, incluyendo espacios y signos de puntuación.
longitud = len(cadena)  # 11

# Slicing (subconjunto de una cadena)
# El slicing permite obtener una parte de la cadena.
# La sintaxis es [inicio:fin:paso], donde "inicio" es el índice del primer carácter a incluir
# y "fin" es el índice donde se detiene (sin incluir ese carácter).
# Si no se especifica "paso", por defecto es 1 (todos los caracteres entre el rango).
subcadena = cadena[0:4]  # "Hola" (los primeros 4 caracteres)

# Slicing con paso
# El parámetro "paso" indica la frecuencia con la que se seleccionan caracteres.
# Un paso de 2 selecciona cada segundo carácter.
subcadena_salto = cadena[::2]  # "Hl,Mno" (cada segundo carácter)

# Invertir una cadena usando slicing
# Usando un paso de -1, se puede invertir una cadena.
cadena_invertida = cadena[::-1]  # "odnuM ,aloH"

# Métodos comunes para trabajar con cadenas:
# .upper() convierte la cadena a mayúsculas.
cadena_mayusculas = cadena.upper()  # "HOLA, MUNDO"

# .lower() convierte la cadena a minúsculas.
cadena_minusculas = cadena.lower()  # "hola, mundo"

# .strip() elimina los espacios en blanco al inicio y al final de la cadena.
cadena_con_espacios = "  Hola, Mundo  "
cadena_sin_espacios = cadena_con_espacios.strip()  # "Hola, Mundo"

# .replace() reemplaza una subcadena por otra.
cadena_modificada = cadena.replace("Mundo", "Python")  # "Hola, Python"

# Búsqueda de subcadenas
# .find() devuelve el índice de la primera aparición de una subcadena, o -1 si no se encuentra.
indice_mundo = cadena.find("Mundo")  # 6