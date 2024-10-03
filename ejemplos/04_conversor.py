import os
""" 
===========================
CONVERSION DE TIPO DE DATOS
===========================

En ocasiones es necesario aplicar conversiones de valores entre tipos de datos para manipular los valores de forma diferente. Por ejemplo, para concatenar valores numéricos con cadenas o representar posiciones decimales en números que se iniciaron como valores enteros:
"""
cadena = "1234"
entero = 45
flotante = 6.2

int(cadena)     # convierte a entero (1234)
float(cadena)   # convierte a coma flotante (1234.0)
str(entero)     # convierte a cadena ("45")
str(flotante)   # convierte a cadena ("6.2")

os.system('cls')
print("===========================\nCONVERSION DE TIPO DE DATOS\n===========================\n")

print("valor_original\ttipo_original\t\ttipo_modificado")
print()
print(cadena, '\t\t', type(cadena),'\t\t', type(int(cadena)))
print(cadena,'\t\t', type(cadena),'\t\t', type(float(cadena)))
print(entero,'\t\t', type(entero),'\t\t', type(str(entero)))
print(flotante,'\t\t', type(flotante),'\t', type(str(flotante)))
print()
