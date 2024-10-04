"""
Este programa calcula el precio final de un producto después de aplicar un descuento:
"""

# Entrada: Solicitar el precio del producto y el porcentaje de descuento
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento (por ejemplo, 10 para 10%): "))

# Proceso: Calcular el monto del descuento y el precio final
monto_descuento = (precio * descuento) / 100
precio_final = precio - monto_descuento

# Salida: Mostrar el precio final después del descuento
print("El precio final después del descuento es:", precio_final)