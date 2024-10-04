"""
Este programa calcula el precio total de un producto incluyendo el IVA (Impuesto al Valor Agregado).
"""

# Entrada: Solicitar el precio del producto y el porcentaje de IVA
precio = float(input("Precio del producto: "))
iva = float(input("Porcentaje de IVA (por ejemplo, 21 para 21%): "))

# Proceso: Calcular el monto del IVA y el precio total
monto_iva = (precio * iva) / 100
precio_total = precio + monto_iva

# Salida: Mostrar el precio total incluyendo IVA
print("El precio total con IVA es:", precio_total)