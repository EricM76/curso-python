'''
 La función input() siempre devuelve una cadena de texto.
 Uso de input() para recibir datos del usuario y validación de datos.
'''

# 1. Solicitar el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")  # input() devuelve una cadena
print("Hola, " + nombre + "!")

# 2. Solicitar edad y convertir a entero
edad = input("¿Cuántos años tienes? ")
edad = int(edad)  # Convertir la entrada a entero
print(f"Tienes {edad} años.")
print(f"En 5 años tendrás {edad + 5} años.")

