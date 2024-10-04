import os
""" 
Este proyecto consiste en una aplicación con Python que permita gestionar 
el inventario de una pequeña tienda o comercio. La aplicación debe ser capaz
de registrar, actualizar, eliminar y mostrar productos en el inventario. 
Además, debe incluir funcionalidades para realizar búsquedas y generar 
reportes de stock.
"""

# Menú de opciones
print(os.system('cls'))
print("============================")
print("Menú de Gestión de Productos")
print("============================\n")
print("1. Alta de productos nuevos")
print("2. Consulta de datos de productos")
print("3. Modificar la cantidad en stock de un producto")
print("4. Dar de baja productos")
print("5. Listado completo de los productos")
print("6. Lista de productos con cantidad bajo mínimo")
print("7. Salir")
# Solicitar al usuario que seleccione una opción
opcion = int(input("Por favor, selecciona una opción (1-7): "))
# Mostramos el nro de la opción seleccionada
print("Has seleccionado:", opcion)


""" REGISTER """


""" UPDATE """


""" DELETE """


""" LIST """


""" SEARCH """


""" GENERATE REPORT """