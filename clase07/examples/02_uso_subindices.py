# Uso de subíndices en listas y tuplas

# Los subíndices permiten acceder a elementos individuales de listas o tuplas.
# Se empieza a contar desde el índice 0.

# Ejemplo con listas
colores = ['rojo', 'verde', 'azul']
print(colores[0])  # Acceder al primer elemento
print(colores[-1])  # Acceder al último elemento usando índices negativos

# Ejemplo con tuplas
numeros = (10, 20, 30, 40)
print(numeros[1])  # Acceder al segundo elemento

# También se pueden usar subíndices para obtener partes de la lista (slicing)
sublista = colores[0:2]  # Del índice 0 al 1 (el último no se incluye)
print(sublista)
