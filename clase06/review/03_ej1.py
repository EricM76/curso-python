
# Inicializar el contador
cantidad_productos = 0


while True:
    nombre_producto = input("Nombre del producto: (salir para finalizar o s) ")
    if nombre_producto.lower() == "salir" or   nombre_producto == "s":
        break
    
    cantidad_productos = cantidad_productos + 1



print(f"total productos ingresados: {cantidad_productos}")
print("FIN DEL SISTEMA")