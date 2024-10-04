""" 
=================
LONGITUD Y ACCESO
=================

A veces es importante saber cuántos caracteres contiene una cadena. Ese valor se lo suele denominar
“longitud”, y se puede obtener muy fácilmente utilizando una función llamada len():
"""

nombre = 'Talento Tech Adultos'
print(len(nombre)) # se imprime 20

"""
Se puede acceder a los elementos de la cadena utilizando subíndices.
El primer caracter tiene subíndice cero. Si usamos subíndices negativos, se cuentan desde el final 
de la cadena.
"""
cadena = "Aprendemos Python"
print(cadena[0]) # A
print(cadena[5]) # d
print(cadena[-1]) # n
print(cadena[-2]) # o


