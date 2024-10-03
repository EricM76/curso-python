""" 
==============
TIPOS DE DATOS
==============
Python es un lenguaje de programación que no requiere especificar el tipo de dato de una variable al declararla. 
Python infiere automáticamente el tipo de dato en tiempo de ejecución según el valor que se le asigna a la variable. Esto proporciona flexibilidad y simplifica la escritura de código.
Recordemos que la forma de asignar el dato a una variable es a través del operador de asignación “=
"""
cadena = "Hola Mundo" # string
entero = 3            # int
flotante = 12.3       # float
logico = True         # boolean

nombre = "Talento Tech"# string
numero = 1234          # int
importe = 35.75        # float
activo = False         # bool


print("==============\nTIPOS DE DATOS\n==============")
print("Hola Mundo",type(cadena))
print(3, type(entero))
print(12.3, type(flotante))
print(True, type(logico))