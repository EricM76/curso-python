""" 
=========================
COMPARACIÓN DE CARACTERES
=========================

Las cadenas de texto se comparan carácter por carácter, siguiendo un orden basado en su codificación
(ASCII o Unicode). Esto significa que Python va a ir chequeando cada carácter de la cadena, de izquierda 
a derecha, hasta que encuentre una diferencia o hasta que una de las cadenas se termine.
"""

print("apple" < "banana")    # True
print("apple" > "Apple")     # True
print("apple" < "apples")    # True

print("python" == "python")  # True
print("Python" != "python")  # True

print("A" < "a")             # True
print("z" > "Z")             # True

"""
Como ves, Python no sólo se fija en si las letras son iguales, sino también en si son mayúsculas o minúsculas,
o si una cadena tiene más o menos caracteres. ¡Esto es súper útil cuando necesitas comparar nombres, 
palabras o cualquier tipo de texto en tus programas!
"""