""" 
=================
SLICING (REBANADO)
=================

El slicing te permite cortar porciones de una cadena de caracteres. Para hacer slicing, usamos corchetes [ ] y dentro indicamos desde qué índice queremos empezar a cortar, y hasta qué índice queremos llegar, separados por dos puntos (:). 
Importante: el índice final que pongas no se incluye, es como decir: "cortame desde acá hasta acá, 
pero sin incluir el último caracter".
"""
# Definimos una cadena
frase = "Aprender Python es divertido"

# Subcadena desde el principio hasta el índice 8 (no inclusive)
subcadena = frase[0:8]

print("Subcadena desde el inicio hasta el índice 8:", subcadena)
#Imprime Subcadena desde el inicio hasta el índice 8: Aprender


"""
Algo interesante del slicing es que podés omitir el índice de inicio o el índice de fin, 
y Python automáticamente va a asumir que querés cortar desde el principio o hasta el final de la cadena, 
respectivamente:
"""
frase = "Aprender Python es divertido"

subcadena = frase[:8] # Subcadena desde el inicio hasta el índice 8 (sin incluirlo)
print("Subcadena desde el inicio hasta el índice 8:", subcadena)
# Imprime Aprender

subcadena = frase[9:] # Subcadena desde el índice 9 hasta el final
print("Subcadena desde el índice 9 hasta el final:", subcadena)
# Imprime Python es divertido


"""
Y todavía hay más. También podés hacer slicing con saltos entre caracteres, usando un tercer parámetro. 
Esto te permite, por ejemplo, tomar sólo cada segundo carácter de una cadena.
"""
texto = "Talento Tech"
subcadena = texto[::2]
print("Subcadena obtenida:", subcadena)
# Imprime TlnoTc

"""
En este ejemplo, con ::2, le indicamos a Python que debe tomar caracteres de dos en dos, 
a partir del primero y hasta llegar al final. 
¡El slicing es una herramienta muy poderosa para cuando necesitás manipular texto en Python!.
"""