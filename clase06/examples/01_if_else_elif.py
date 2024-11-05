# Estructuras condicionales en Python: if, else, elif

# if: se utiliza para ejecutar un bloque de código si la condición es verdadera.
# elif: permite evaluar múltiples condiciones si la anterior no fue verdadera.
# else: se ejecuta si ninguna de las condiciones anteriores es verdadera.


# Ejemplo: Verificación de números pares o impares
numero = 10
if numero % 2 == 0: # 0 == 0 --> if True:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")



# Ejemplo: Uso de if, elif y else
edad = 30
if edad < 18:
    print("Eres menor de edad.")
elif edad < 30:
    print("Eres joven.")
elif edad < 50:
    print("Camino a ser adulto.")
else:
    print("Eres adulto.")


# Algo complejo
# Ejemplo: Uso de if, elif y else
altura = 1.67
edad = 30
if edad < 18:
    print("Eres menor de edad.")
elif edad < 30:
    print("Eres joven.")
    if edad == 24:
        print("Hola")
    elif edad == 25:
        if altura <= 1.5:
            print("Hola!!!")
        else:
            print("Hola!")
    else:
        print("Chau")
elif edad < 50:
    print("Camino a ser adulto.")
else:
    print("Eres adulto.")



