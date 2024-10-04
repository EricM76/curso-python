"""
Este programa calcula el costo total de varios artículos comprados, basándose en el precio unitario y la cantidad comprada:
"""

# Entrada: Solicitar el precio unitario y la cantidad de artículos
precio_unitario = float(input("Ingresa el precio unitario del artículo: "))
cantidad = int(input("Ingresa la cantidad de artículos comprados: "))

# Proceso: Calcular el costo total
costo_total = precio_unitario * cantidad

# Salida: Mostrar el costo total de la compra
print("El costo total de la compra es:", costo_total)
