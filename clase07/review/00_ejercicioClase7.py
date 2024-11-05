'''
Consultar el stock de productos
Tu programa debe permitir consultar el inventario de una tienda para verificar si un producto
está en stock. Si el producto está en la lista, el programa debe informarlo, si no, debe
mostrar un mensaje indicando que no está disponible.
Tips:
● Usá una lista para almacenar los productos en stock.
● Permití que el usuario ingrese el nombre de un producto a consultar.
● Recorré la lista con un bucle while para verificar si el producto está en stock.

'''


animales=["leon",
          "tero",
          "perro"]

temperaturas = [23.5, 29, 87.3]

# lista_productos = [producto1,producto2,.......,pruducton]

'''
cada producto va a ser una lista con el siguiente formato
[nombredelPraducto(str), stock(int)] --> ["martillo", 34]
["alicate", 3] [89, "destornilladores"]
'''

lista_productos = [
    ["martillo", 34], # indice 0
    ["alicate", 3],
    ["tijera", 15],
    ["mar", 56], # indice 3
    ["ali", 3],
    ["tij", 15],
    ["ma", 34],
    ["al", 3],
    ["ti", 15],      # indice 8
    ["tij", 15],
    ["ma", 34],
    ["alcohol", 3]
]


productoABuscar = input("Producto: ") # "mar"


indice = 0
while  indice < len(lista_productos):
    producto = lista_productos[indice] # ["mar", 56]
    if productoABuscar == producto[0]:
        print(producto)
        if producto[1] < 20:
            print("Pedir mas al proveedor")
        break
    indice = indice + 1


# indice=7
# print(lista_productos[indice])



# agregar un producto

nombre = input("Nombre ")
stock = int(input("Cant "))



lista_productos.append([nombre, stock])


print(lista_productos)
