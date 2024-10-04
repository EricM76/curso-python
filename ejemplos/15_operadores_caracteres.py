""" 
==========
OPERADOR *
==========

Hay que tener en cuenta que en Python algunos operadores tienen
una función ligeramente diferente según el contexto en que se
usan. Por ejemplo,hemos visto que con * podemos multiplicar
números. Pero si lo usamos con una cadena y un número, en ese
orden, replicamos la cadena. ¡Probalo!
"""

risa = 'ja'
carcajada = risa * 5 # jajajajaja
linea = "-" * 15 # ---------------

print(risa)
print(carcajada)
print(linea)

""" 
==========
OPERADOR +
==========

Para unir (concatenar) dos o más cadenas se utiliza el operador + (más). 
No funciona con tipos mixtos; para evitar errores, tenemos que usar las funciones de conversión.
"""
nombre = input("Ingrese su nombre: ") # Juan
saludo = "Hola " + nombre
print(saludo) # Hola Juan

var1 = 3 + 5 # 8 (entero)
var2 = "3" + "5" # 35 (cadena)
var3 = 3 + "5" # TypeError
var4 = str(3) + "5" # 35 (cadena)
var5 = 3 + int("5") # 8 (entero)