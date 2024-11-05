'''
Compra con descuentos

Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes
reglas:

Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000,
aplica un descuento del 15%.

Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento
del 10%.

Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.

Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier
descuento o simplemente el monto original si no hay descuento.

'''

monto_total = input("Monto total: ")
monto_total = float(monto_total)
# monto_total = 1156666

cantidad = input("Cantidad de articulos: ")
cantidad = int(cantidad)

'''
Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.
'''

if cantidad >= 5 and monto_total > 10000:
    monto_total = monto_total * 0.85
elif cantidad < 5 and cantidad >= 3:
    monto_total = monto_total * 0.9


print(f"Me debes: {monto_total}")
