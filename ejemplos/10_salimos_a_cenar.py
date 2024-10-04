import os;

"""
Vamos a escribir un programa que calcule el costo total de una salida a cenar para un grupo 
de personas. En el mismo se pide la cantidad de personas, el precio promedio del plato y 
una propina fija del 10%.
"""

os.system('cls')
# Pedir la cantidad de personas
personas = int(input("¿Cuántas personas van a cenar?: "))

# Pedir el precio promedio del plato por persona
precio_plato = float(input("¿Cuál es el precio promedio del plato?: "))

# Calcular el total de la cena (sin propina)
total_cena = personas * precio_plato

# Calcular la propina (10%)
propina = total_cena * 0.10

# Calcular el total final con propina
total_con_propina = total_cena + propina

# Mostrar los resultados
# print("Total de la cena (sin propina): ", total_cena)
# print("Propina (10%): ", propina)
# print("Total a pagar (con propina): ", total_con_propina)

print(f"Total de la cena (sin propina): {total_cena:.2f}")
print(f"Propina (10%): {propina:.2f}")
print(f"Total a pagar (con propina): {total_con_propina:.2f}")