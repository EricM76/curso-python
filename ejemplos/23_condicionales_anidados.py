""" 
======================
CONDICIONALES ANIDADOS
======================

Hasta ahora, vimos cómo if y else te permiten tomar decisiones en tu programa, pero ¿qué pasa cuando 
necesitás evaluar más de una condición a la vez? Acá es donde entran en juego las estructuras 
condicionales anidadas. 
"""
nota = 85

if nota >= 60:
   print("¡Aprobaste!")
   if nota >= 90:
       print("¡Excelente calificación!")
   else:
       if nota >= 75:
           print("Muy buen trabajo.")
       else:
           print("Buen esfuerzo, pero hay margen de mejora.")
else:
   print("No alcanzaste la calificación mínima para aprobar.")
"""
Este concepto puede sonar un poco complicado al principio, pero en realidad es bastante intuitivo: 
se trata de poner una condición dentro de otra. Esto te permite manejar situaciones donde la decisión 
que vas a tomar depende de una serie de condiciones que deben evaluarse en secuencia.
"""

color = input("¿Cuál es el color del semáforo? ")

if color:
    print("Según el color la acción es:")
    if color == "rojo":
        print("PARAR")
    elif color == "amarillo":
        print("TENER PRECAUCIÓN")
    elif color == "verde":
        print("AVANZAR")
    else:
        print("NINGUNA. COLOR DESCONOCIDO")
else :
    print("DEBE PROPORCIONAR UN COLOR")