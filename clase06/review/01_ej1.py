'''

Control de stock de productos:
Desarrollá un programa que permita a quienes interactúen con él ingresar el nombre de
varios productos y la cantidad en stock que hay de cada uno. 
El programa debe seguir
pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" como
nombre de producto. Después de que el bucle termine el programa debe mostrar la cantidad
total de productos ingresados.
Tips:
● Vas a necesitar un contador.
● Tené presente las estructuras condicionales.


uva 56
banana 65
pera 489
salir

total productos ingresadios: 3

'''



'''
hacer hasta que sea salir
    ingresar nombre de producto
    incrementar un contador

'''

# Inicializar el contador
cantidad_productos = 0
#inicializando una variable de control
nombre_producto = "s"

while nombre_producto != "salir":
    nombre_producto = input("Nombre del producto: ")
    cantidad_productos = cantidad_productos + 1
    # if nombre_producto != "salir":
    #     cantidad_productos = cantidad_productos + 1



    # if nombre_producto == "salir":
    #     cantidad_productos = cantidad_productos -  1


cantidad_productos = cantidad_productos - 1
print(f"total productos ingresados: {cantidad_productos}")
print("FIN DEL SISTEMA")