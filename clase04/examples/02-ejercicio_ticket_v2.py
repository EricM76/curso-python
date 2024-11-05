""" 
Ticket de compra
¡Vamos a crear tu propio ticket de compra! El desafío es escribir un programa que le pida al
usuario el nombre, la cantidad y el valor unitario de tres productos. Después, tu programa
tiene que calcular el importe de IVA (21%) de cada uno y mostrar en la terminal un ticket de
compra con todos los datos. 
"""


# Solicitar el nombre, la cantidad y el valor unitario de tres productos
""" nombre1 = input("Ingresá el nombre del primer producto: ")
cantidad1 = int(input("Ingresá la cantidad: "))
valor_unitario1 = float(input("Ingresá el valor unitario: "))
nombre2 = input("Ingresá el nombre del segundo producto: ")
cantidad2 = int(input("Ingresá la cantidad: "))
valor_unitario2 = float(input("Ingresá el valor unitario: "))
nombre3 = input("Ingresá el nombre del tercer producto: ")
cantidad3 = int(input("Ingresá la cantidad: "))
valor_unitario3 = float(input("Ingresá el valor unitario: ")) """
nombre1 = "pan de salvado"
cantidad1 = 5
valor_unitario1 = 12.5
nombre2 = "Azucar negra"
cantidad2 = 1
valor_unitario2 = 58.3
nombre3 = "Zapallo"
cantidad3 = 5
valor_unitario3 = 12.56
# Calcular el importe de IVA (21%) para cada producto
iva1 = (valor_unitario1 * cantidad1) * 0.21
iva2 = (valor_unitario2 * cantidad2) * 0.21
iva3 = (valor_unitario3 * cantidad3) * 0.21
# Calcular el costo total de cada producto (sin IVA)
costo1 = valor_unitario1 * cantidad1
costo2 = valor_unitario2 * cantidad2
costo3 = valor_unitario3 * cantidad3
# Calcular el total con IVA
total_con_iva1 = costo1 + iva1
total_con_iva2 = costo2 + iva2
total_con_iva3 = costo3 + iva3
# Mostrar el ticket de compra simulado
print("\n--- TICKET DE COMPRA ---")
# print("Cantidad\tDescripción\t\tPrecio Unitario\t\tTotal")
print(f"{'Cantidad':16}{'Descripción':24}{'Precio Unitario':24}{'Total'}")
print(f"{cantidad1:<16}{nombre1:<24}{valor_unitario1:<24.2f}{total_con_iva1:^.2f}")
print(f"{cantidad2:<16}{nombre2:<24}{valor_unitario2:<24.2f}{total_con_iva2:^.2f}")
print(f"{cantidad3:<16}{nombre3:<24}{valor_unitario3:<24.2f}{total_con_iva3:^.2f}")

print("-------------------------------------------")
# Calcular el total neto y el IVA total
total_neto = costo1 + costo2 + costo3
iva_total = iva1 + iva2 + iva3
total_general = total_con_iva1 + total_con_iva2 + total_con_iva3
# Mostrar el total neto, IVA y total general
print(f"{'':50}{'Total Neto:':<10}{total_neto:>12.2f}")
print(f"{'':50}{'IVA:':<10}{iva_total:>12.2f}")
print(f"{'':50}{'Total:':<10}{total_general:>12.2f}")
