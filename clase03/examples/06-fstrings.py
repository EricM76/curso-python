
mes1 = 5800
mes2 = 4800
mes3 = 6780
mes4 = 5690
mes5 = 5840
mes6 = 3550

promedio = (mes1 + mes2 + mes3 + mes4 + mes5 + mes6) / 6

auxiliar = type(promedio)


promedio = str(promedio) # 5410.0 --> "5410.0"
print("El ingreso promedio en el semestre es de " + promedio + ".-\nMeses: \nmes 1: " + str(mes1)+ "\nmes 2: " + str(mes2) )
print(f"{promedio}")

print(f"👌El ingreso promedio en el semestre es de {promedio}.-\n Meses: \n     mes 1: {mes1} \nmes 2: {mes2}")
