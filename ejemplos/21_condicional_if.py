""" 
==============
CONDICIONAL IF
==============

Las estructuras condicionales tienen como objetivo ejecutar un bloque de instrucciones u otro en base a 
una condición que puede ser verdadera o falsa. La palabra clave asociada a esta estructura es if.

Si la condición es True se ejecuta el bloque dentro del if. Luego, independientemente del valor de verdad 
de la condición.
"""
nota = float(input("Nota: "))

if nota >= 7:
  print("Aprobado.")

"""
Esa pequeña sangría al principio de la línea no es sólo por estilo; le dice a Python que esas líneas 
de código forman parte del bloque del if. No colocarla arroja un error.
"""