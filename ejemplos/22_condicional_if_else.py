""" 
===================
CONDICIONAL IF ELSE
===================

Ya vimos cómo if le da la capacidad a tu programa de tomar decisiones cuando una condición es verdadera. 
Pero, ¿qué pasa cuando esa condición no se cumple? 

Ahí es donde entra en juego else. Mientras que if se encarga de ejecutar un bloque de código solo si 
algo es True, else viene al rescate cuando esa condición resulta ser False.
"""
edad = input("Dime tu edad: ")

if edad >= 18:
  # Bloque de instrucciones que se
  # ejecuta si la condición es verdadera
  print("Puedes pasar.")
else:
  # Bloque de instrucciones que se
  # ejecuta si la condición es falsa
  print("No admitido.")

"""
Preguntamos si edad es mayor o igual que 18. Si es verdad, mostramos “Puedes pasar.” y el programa 
continúa sin ejecutar el bloque del else. Si es falso, mostramos “No admitido.” y obviamos el bloque del if.
"""

edad = int(input("Ingresá tu edad: "))
tiene_licencia = input("¿Tenés licencia de conducir? (S/N): ")

# Verificamos si la persona puede conducir
if edad >= 18 and tiene_licencia == "S":
   print("Podés conducir.")
else:
   print("No podés conducir.")

"""
Si alguna de las dos condiciones no se cumple (por ejemplo, si la persona no tiene 18 años 
o si no tiene licencia), el programa saltará al else y mostrará "No podés conducir.".
"""