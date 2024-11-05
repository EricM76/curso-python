
# Inicializar el contador
cantidad_productos = 0
#inicializando una variable de control
nombre_producto = "suuuu"

while not (nombre_producto.lower() == "salir" or   nombre_producto == "s"):
    nombre_producto = input("Nombre del producto: (salir para finalizar o s) ")
    cantidad_productos = cantidad_productos + 1
    # if nombre_producto != "salir":
    #     cantidad_productos = cantidad_productos + 1



    # if nombre_producto == "salir":
    #     cantidad_productos = cantidad_productos -  1


cantidad_productos = cantidad_productos - 1
print(f"total productos ingresados: {cantidad_productos}")
print("FIN DEL SISTEMA")