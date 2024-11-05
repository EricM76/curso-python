# Métodos de listas y tuplas

# Métodos comunes de las listas
mi_lista = [4, 2, 8, 6]
mi_lista.append(10)        # Agrega un elemento al final
mi_lista.remove(2)         # Elimina el primer valor igual a 2
mi_lista.sort()            # Ordena la lista
mi_lista.reverse()         # Invierte el orden de los elementos

# Ejemplo con los métodos de listas
print("Lista ordenada:", mi_lista)

# Métodos de tuplas (limitados debido a que las tuplas son inmutables)
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla.count(3))   # Cuenta cuántas veces aparece el número 3
print(mi_tupla.index(4))   # Retorna el índice de la primera aparición del número 4

# Diferencias: las listas tienen muchos métodos para agregar, quitar y modificar, mientras que las tuplas no.
