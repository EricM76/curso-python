'''
Ejercicio Práctico #2
Ingreso promedio
Escribir un programa que guarde en variables el monto del ingreso de cada uno de los
primeros seis meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx”
donde “xxxxx” es el valor calculado.
'''


mes1 = 5800
mes2 = 4800
mes3 = 6780
mes4 = 5690
mes5 = 5840
mes6 = 3550

promedio = (mes1 + mes2 + mes3 + mes4 + mes5 + mes6) / 6

auxiliar = type(promedio)

#print(auxiliar)
print(type(promedio))

# print("El ingreso promedio en el semestre es de " + str(promedio))

# Python es dinamicamente tipado
promedio = str(promedio) # 5410.0 --> "5410.0"
print("El ingreso promedio en el semestre es de " + promedio)

