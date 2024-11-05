
#El INPUT Siempre retorna un str
nombre = input("Dame tu nombre")

edad = input("Che, ingresa tu edad: ")
edad = int(edad)

# edad = int(input("Che, ingresa tu edad: "))


edadEndiezAnios = edad + 10 # Concatenacion "14" + 10

print(f"Hola {nombre}, tu edad en diez años serà de {edadEndiezAnios} años")