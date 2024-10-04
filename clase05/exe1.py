"""
=====================
CONTROL DE INVENTARIO
=====================

Imagina que estás ayudando a una tienda de videojuegos a organizar su inventario. 
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, 
si no hay, que avise que hay que reponerlo. 

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.
"""

stock_actual = 10

cantidad_solicitada = int(input("¿Qué cantidad necesita? "))

if cantidad_solicitada > stock_actual :
    print("No hay STOCK suficiente. Debe hacer un nuevo pedido")
else :
    stock_actual = stock_actual - cantidad_solicitada
    print(f"STOCK actualizado. Nuevo STOCK : {stock_actual} ")