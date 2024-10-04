import os
"""
===================
TICKET DE LA COMPRA
===================

Escribir un programa que solicite el nombre, la cantidad y el valor unitario de tres productos.
Luego, debe calcular el importe de IVA (21%) de cada producto.
Por último, debe mostrar en la terminal el ticket de la operación con todos los datos de la compra

"""
print(os.system('cls'))

producto_1 = input("Ingrese el nombre del producto: ")
valor_1 = float(input("Ahora ingrese el valor del producto '" + producto_1 + "': "))
print(f"{producto_1} - ${valor_1}")
print()

producto_2 = input("Ingrese el nombre del producto: ")
valor_2 = float(input("Ahora ingrese el valor del producto '" + producto_2 + "': "))
print(f"{producto_2} - ${valor_2}")
print()

producto_3 = input("Ingrese el nombre del producto: ")
valor_3 = float(input("Ahora ingrese el valor del producto '" + producto_3 + "': "))
print(f"{producto_3} - ${valor_3}")
print()

valor_1_mas_IVA = valor_1 + (valor_1 * .21)
valor_2_mas_IVA = valor_2 + (valor_2 * .21)
valor_3_mas_IVA = valor_3 + (valor_3 * .21)

print("""
===================
TICKET DE LA COMPRA
===================
""")

print(f"{producto_1} + IVA \t {valor_1_mas_IVA}")
print(f"{producto_2} + IVA \t {valor_2_mas_IVA}")
print(f"{producto_3} + IVA \t {valor_3_mas_IVA}")
print()
print(F"TOTAL \t\t {valor_1_mas_IVA + valor_2_mas_IVA + valor_3_mas_IVA}")