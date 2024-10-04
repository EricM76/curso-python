import os
"""
======================
CONSUMO DE COMBUSTIBLE
======================

Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que consume un coche por cada 100 km de recorrido, 
el costo de cada litro de combustible y la longitud del viaje realizado (en kilómetros), 
muestra un detalle de los litros consumidos y el dinero gastado.

"""
print(os.system('cls'))

consumo_por_km = float(input("Consumo de combustible (en lts) cada 100km: "))
precio_por_litro = float(input("Precio por litro de fafta: "))
kilometros = float(input("Kilómetros recorridos: "))
consumo_litros = kilometros * consumo_por_km
dinero_gastado = consumo_litros * precio_por_litro
(print)

print("""
======================
CONSUMO DE COMBUSTIBLE
======================
""")

print(f"Rendimiento: {consumo_por_km} litros por cada 100km")
print(f"Precio del combustible (x litro): {precio_por_litro}")
print(f"Kilómetros recorridos: {kilometros}")
print()
print(f"Litros consumidos: {consumo_litros}")
print(f"Dinero gastado: {dinero_gastado}")