# Las listas y tuplas son estructuras de datos que permiten almacenar colecciones de elementos.

# Lista: se puede modificar (es mutable).
lista_ejemplo = [1, 2, 3, 4, 5]

# Tupla: no se puede modificar (es inmutable).
tupla_ejemplo = (1, 2, 3, 4, 5)

# Ejemplo de creación
mi_lista = ['manzana', 'banana', 'cereza']
mi_tupla = ('manzana', 'banana', 'cereza')

# Manipulación de listas (agregar, eliminar, modificar)
mi_lista.append('naranja')  # Agregar un elemento al final
print(mi_lista)  # ['manzana', 'banana', 'cereza', 'naranja']

mi_lista[1] = 'frutilla'  # Modificar un elemento
print(mi_lista)  # ['manzana', 'frutilla', 'cereza', 'naranja']

mi_lista.pop(0)  # Eliminar el primer elemento
print(mi_lista)  # ['frutilla', 'cereza', 'naranja']

# --- Métodos adicionales para listas ---

# Método insert(): Insertar un elemento en una posición específica
mi_lista.insert(1, 'kiwi')  # Inserta 'kiwi' en el índice 1
print(mi_lista)  # ['frutilla', 'kiwi', 'cereza', 'naranja']

# Método remove(): Eliminar el primer elemento que coincide con el valor dado
mi_lista.remove('cereza')  # Elimina la primera aparición de 'cereza'
print(mi_lista)  # ['frutilla', 'kiwi', 'naranja']

# Método extend(): Agregar múltiples elementos de otra lista al final
mi_lista.extend(['mango', 'pera'])  # Agrega varios elementos al final
print(mi_lista)  # ['frutilla', 'kiwi', 'naranja', 'mango', 'pera']

# Método sort(): Ordenar la lista
mi_lista.sort()  # Ordena la lista alfabéticamente
print(mi_lista)  # ['frutilla', 'kiwi', 'mango', 'naranja', 'pera']

# Método reverse(): Invertir el orden de los elementos de la lista
mi_lista.reverse()  # Invierte el orden de la lista
print(mi_lista)  # ['pera', 'naranja', 'mango', 'kiwi', 'frutilla']

# --- Tuplas ---
# Las tuplas son inmutables, lo que significa que no podemos modificar sus elementos directamente.
# Por ejemplo, no podemos hacer esto: mi_tupla[1] = 'frutilla'  # Esto daría error

# Sin embargo, podemos acceder a sus elementos:
print(mi_tupla[0])  # 'manzana'

# Podemos convertir una tupla en una lista si queremos modificarla:
mi_lista_desde_tupla = list(mi_tupla)  # Convierte la tupla en una lista
mi_lista_desde_tupla.append('uva')  # Ahora podemos modificar la nueva lista
print(mi_lista_desde_tupla)  # ['manzana', 'banana', 'cereza', 'uva']

# Si es necesario, también podemos convertir una lista en una tupla:
mi_nueva_tupla = tuple(mi_lista_desde_tupla)
print(mi_nueva_tupla)  # ('manzana', 'banana', 'cereza', 'uva')
