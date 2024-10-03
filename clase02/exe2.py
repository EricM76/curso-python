import os
""" 
INGRESO PROMEDIO

Escribir un programa que guarde en variables el monto del ingreso de cada uno de los primeros 6 meses del año.
Luego, calcular y guardar en otra variable el promedio de esos valores.
Por último, mostrar una leyenda que diga “El ingreso promedio en el semestre es de xxxxx” donde “xxxxx” es el valor calculado. 
"""

ene=1000
feb=1300
mar=3000
abr=5000
may=4300
jun=7000

promedio=(ene+feb+mar+abr+may+jun)/6

os.system("cls")
print("================\nINGRESO PROMEDIO\n================")
print("El ingreso promedio en el semestre es de " + str(round(promedio)))
print()