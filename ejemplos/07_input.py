import os;

os.system('cls')
print("=============\nFUNCIÓN INPUT\n=============\n")


print("""
La función input() proporciona un mecanismo para que el usuario introduzca datos en nuestro programa. 
Muestra el cursor en la terminal, lee lo que se escribe, y cuando se presiona Enter, este contenido, 
en formato de cadena de caracteres, se puede asignar a una variable.
""")

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)
print()

print("""
Dado que input() devuelve únicamente valores tipo string, es necesario realizar una conversión 
a algún formato numérico si se requiere operar matemáticamente con esos valores.
Para ello, usamos las funciones int() y float():
""")

num1 = input("Ingrese un número: ")
numero = float(num1)
resultado = numero * 2
print(numero,"x 2 =", resultado)
