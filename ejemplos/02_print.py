""" 
==================
LA FUNCIÓN PRINT()
==================
La función print() permite mostrar datos en la terminal. Recibe entre paréntesis lo que se conoce como parámetros, que pueden ser variables y/o literales, separados por comas. Las cadenas pueden delimitarse con comillas simples o dobles.
Luego de imprimir, print() realiza un salto de línea (pasa a la línea siguiente). Si se usa print() sin argumentos, sólo se muestra la línea en blanco:
"""
print("\n==================\nLA FUNCIÓN PRINT()\n==================")
print("Linea 1")
print()
print("Linea 2")

""" 
En este ejemplo, además de la creación y asignación de valores a variables y el uso de algunos operadores, vemos como utilizar print() para mostrar literales y valores de variables en la terminal:
"""
nombre = "Talento Tech"
a = 20
b = 30
promedio = (a + b) / 2

print("\n===========================\nLA FUNCIÓN PRINT(): Ejemplo\n===========================")
print("Nombre:", nombre)
print("La suma de",a,"y",b,"es",a+b)
print("Promedio:", promedio)

"""
======================
LA FUNCIÓN PRINT():end
======================
end=' ' es un parámetro opcional de la función print() y determina qué se debe imprimir al final de cada llamada a la función. Por defecto es un carácter de nueva línea ('\n'), lo que significa que cada llamada a print() agrega automáticamente una nueva línea al final.
Al cambiar end a una cadena nula ('  ')  con un espacio en blanco, modificamos su comportamiento:
"""
print("\n========================\nLA FUNCIÓN PRINT(): end\n========================")
print("¡Hola Mundo!", end=" ")
print("Aprendiendo Python.")

"""
======================
LA FUNCIÓN PRINT():\n
======================
\n (nueva línea) representa un carácter especial que se utiliza para insertar una nueva línea en una cadena de texto. Cuando escribimos \n dentro de una cadena y la imprimimos, el texto que le sigue se coloca en una nueva línea:
"""
print("\n====================================\nLA FUNCIÓN PRINT(): 'salto de línea' \n====================================")
print("Escribimos\nen\nvarias\nlíneas.")

"""
======================
LA FUNCIÓN PRINT():\t
======================
\t (tabulación) se utiliza para insertar un tabulador (o tabulación) en una cadena de texto. Cuando Python encuentra \t dentro de una cadena a imprimir, inserta un espacio equivalente al de una tabulación
El comportamiento exacto de \t depende de la longitud de las cadenas que lo rodean. La tabulación agrega un número fijo de espacios, y si las cadenas son más largas o más cortas de lo esperado, la alineación puede verse afectada.

"""
print("\n=================================\nLA FUNCIÓN PRINT(): 'tabulación' \n=================================")
print("Nombre \tApellido \tEdad")
print("Juan \tFernández \t32")