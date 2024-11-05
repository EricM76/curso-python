# Bucle while en Python

# El bucle while repite un bloque de código mientras una condición sea verdadera.

# Ejemplo 1: Bucle infinito (cuidado con esto)
# while True:
#     print("Esto se repetirá indefinidamente.")

# Ejemplo 2: Bucle controlado
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1  # Incrementamos el contador para evitar un bucle infinito







# Ejemplo 3: Uso de break para salir del bucle
while True:  
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower() == 'n':
        print("Saliendo del bucle...")
        break


