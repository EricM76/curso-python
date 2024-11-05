

"""
banana 99.9
pera 88.8
uva 7.1
"""

frutas = []
while True:
    nombreProducto = input("Ingresa nombre de producto(s para salir) ")
    if nombreProducto.lower() =="s":
        print("carga Finalizada")
        break
    precio = float(input("Precio ? "))
    # lista producto
    producto = []
    producto.append(nombreProducto)
    producto.append(precio)
    # ["banana", 99.9]
    frutas.append(producto)
    #frutas.append([nombreProducto,precio])


print(frutas)
    