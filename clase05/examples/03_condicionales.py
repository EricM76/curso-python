# Control de flujo con condicionales

# if: ejecuta un bloque de código si una condición es verdadera
numero = 5
if numero > 0:
    print("El número es positivo")

# else: ejecuta un bloque si la condición del if es falsa
if numero < 0:
    print("El número es negativo")
else:
    print("El número no es negativo")  # Se ejecuta porque numero >= 0

# elif: agrega más condiciones a la estructura
if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# Ejemplo: verificando la calificación de un estudiante
calificacion = 85
if calificacion >= 90:
    print("Sobresaliente")
elif calificacion >= 80:
    print("Notable")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Insuficiente")
