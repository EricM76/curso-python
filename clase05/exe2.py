"""
=====================
COMPRA CON DESCUENTOS
=====================

Escribe un programa en Python que solicite al usuario el monto total de la compra y la cantidad de 
artículos que está comprando. El programa debe determinar el descuento aplicable según las siguientes reglas:

-   Si la cantidad de artículos comprados es mayor o igual a 5 y el monto total es mayor a $10000, 
    aplica un descuento del 15%.
-   Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a 3, aplica un descuento del 10%.
-   Si la cantidad de artículos comprados es menor a 3, no se aplica descuento.

Al final, el programa debe imprimir el monto total de la compra después de aplicar cualquier descuento 
o simplemente el monto original si no hay descuento.
"""

monto_total = float(input("Ingrese el monto total de la compra: "))
cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
descuento = 0

if cantidad_articulos > 5 and monto_total > 10000 :
    descuento = 15 * monto_total / 100
    monto_total = monto_total - descuento
elif cantidad_articulos < 5 and cantidad_articulos >= 3:
    descuento = 10 * monto_total / 100
    monto_total = monto_total - descuento

print(f"Total a pagar: {monto_total}")