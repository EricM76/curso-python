'''
Conversión entre tipos de datos y salida de datos en Python.
Casting: Proceso de conversión explícita entre tipos de datos, como de entero a flotante, o viceversa.
Funciones de conversión: int(), float(), str(), bool().
'''
# 1. Conversión de entero a flotante
numero_entero = 7
numero_decimal = float(numero_entero)  # Convertimos un entero a un flotante
print("Convertido a flotante: " + str(numero_decimal))

# 2. Conversión de flotante a entero
numero_decimal = 9.99
numero_entero = int(numero_decimal)    # Convertimos un flotante a entero. Los decimales se descartan.
print("Convertido a entero: " + str(numero_entero))

# 3. Conversión a cadena de texto
numero = 123
cadena = str(numero)                   # Convertimos un entero a una cadena de texto
print(f"Convertido a cadena: '{cadena}'")

# 4. Conversión de cadena de texto a entero
cadena_numero = "456"
numero_convertido = int(cadena_numero) # Convertimos una cadena de texto que representa un número a entero
print(f"Cadena '456' convertida a entero: {numero_convertido}")

# 5. Conversión a booleano
cadena_vacia = ""
cadena_no_vacia = "Hola"
booleano_vacio = bool(cadena_vacia)    # Convertimos una cadena vacía a booleano (False)
booleano_no_vacio = bool(cadena_no_vacia) # Convertimos una cadena no vacía a booleano (True)
print("Cadena vacía como booleano: " + str(booleano_vacio))
print(f"Cadena no vacía como booleano: {booleano_no_vacio}")
