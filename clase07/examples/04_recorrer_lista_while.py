# Recorrer una lista con while

# Se puede recorrer una lista usando un bucle while y un contador como índice.

frutas = ['manzana', 'banana', 'cereza', 'naranja']
indice = 0

while indice < len(frutas):
    print(f"Fruta en índice {indice}: {frutas[indice]}")
    indice += 1  # Incrementamos el índice en cada iteración

# Ejemplo con condicionales dentro del bucle
numeros = [10, 25, 30, 45]
i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        print(f"{numeros[i]} es par.")
    else:
        print(f"{numeros[i]} es impar.")
    i += 1
