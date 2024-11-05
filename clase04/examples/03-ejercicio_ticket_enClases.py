""" 
Ticket de compra
¡Vamos a crear tu propio ticket de compra! El desafío es escribir un programa que le pida al
usuario el nombre, la cantidad y el valor unitario de tres productos. Después, tu programa
tiene que calcular el importe de IVA (21%) de cada uno y mostrar en la terminal un ticket de
compra con todos los datos. 
"""

# ENTRADAS
# Solicitar el nombre, la cantidad y el valor unitario de tres productos

"""nombre_producto1 = input("Nombre producto 1: ") # "pera"
cantidad_producto1 = input("Cantidad ? ") # "1.5"
cantidad_producto1 = float(cantidad_producto1) # 1.5
precio_producto1 = float(input("Precio ? ")) # 2000.0

nombre_producto2 = input("Nombre producto 2: ") # "pera"
cantidad_producto2 = input("Cantidad ? ")
cantidad_producto2 = float(cantidad_producto2)
precio_producto2 = float(input("Precio ? "))

nombre_producto3 = input("Nombre producto 3: ") # "pera"
cantidad_producto3 = input("Cantidad ? ")
cantidad_producto3 = float(cantidad_producto3)
precio_producto3 = float(input("Precio ? "))"""


nombre_producto1 = "Pera"
cantidad_producto1 = 1.5
precio_producto1 = 2000.0

nombre_producto2 = "Manzana"
cantidad_producto2 = 5
precio_producto2 = 5500

nombre_producto3 = "MandarIna"
cantidad_producto3 = 2.35
precio_producto3 = 6850.0



# PROCESO
# Calcular el importe de IVA (21%) para cada producto
iva_producto1 = precio_producto1 * 0.21
iva_producto2 = precio_producto2 * 0.21
iva_producto3 = precio_producto3 * 0.21
# Calcular el costo total de cada producto (sin IVA)
costo_total_producto1 = precio_producto1 * cantidad_producto1 # 2000.0 * 1.5 --> 3000.0
costo_total_producto2 = precio_producto2 * cantidad_producto2
costo_total_producto3 = precio_producto3 * cantidad_producto3

# Calcular el total neto y el IVA total
total_neto = costo_total_producto1 + costo_total_producto2 + costo_total_producto3
iva_total = total_neto * 0.21


# SALIDAS
# Mostrar el ticket de compra simulado

print("Ticket de compra")
print(f"Producto\t\t Cantidad Precio")
print(f"{nombre_producto1.upper():24} {cantidad_producto1:<8.2f} {precio_producto1:.3f}")
print(f"{nombre_producto2:24} {cantidad_producto2:<8.2f} {precio_producto2:.3f}")
print(f"{nombre_producto3:24} {cantidad_producto3:<8.2f} {precio_producto3:.3f}")


# Mostrar el total neto, IVA y total general

