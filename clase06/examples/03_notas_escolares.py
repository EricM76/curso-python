
acumulador = 0
contador = 0

while True:  
    nota = int(input("Nota: "))
    # if nota > 10:
    #     continue
    acumulador = acumulador + nota
    contador = contador + 1
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower() == 'n':
        print("Saliendo del bucle...")
        break

promedio = acumulador / contador

print(promedio)