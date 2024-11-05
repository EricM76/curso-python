# Ejemplo 1: Recorrer una lista con un bucle for
# Los bucles for se usan para iterar sobre una secuencia (lista, cadena, etc.)

frutas = ["manzana", "banana", "cereza","banana"]

# Usamos un bucle for para imprimir cada fruta de la lista
for fruta in frutas:
    print(fruta)  # Se imprime cada elemento de la lista

# Ejemplo 2: Usar for con un rango de números
# La función range(n) genera una secuencia de números de 0 a n-1
for i in range(5):
    print(i)  # Se imprime 0, 1, 2, 3, 4

# Ejemplo 3: Recorrer una lista usando índice
# Podemos usar el rango basado en la longitud de la lista para acceder a los elementos por su índice
for i in range(len(frutas)):
    print(f"Fruta en índice {i}: {frutas[i]}")  # Se accede a cada elemento por su índice

for j in frutas:
    print(j)