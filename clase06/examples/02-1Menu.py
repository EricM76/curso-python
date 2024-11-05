

nro1 = 4
nro2 = 5
opcion = 1

while opcion != 0:

    print("1 Sumar")
    print("2 Restar")
    print("3 Multiplicar")
    print("4 Dividir")
    print("0 Salir")

    opcion = input("Opcion ?: ")
    opcion = int(opcion)

    if opcion == 1:
        resultado = nro1 + nro2
        print(f"EL resultado de la operacion (Suma) es {resultado}")
    elif opcion == 2:
        resultado = nro1 - nro2
        print(f"EL resultado de la operacion (Resta) es {resultado}")
    elif opcion == 3:
        resultado = nro1 * nro2
        print(f"EL resultado de la operacion (Multiplicacion) es {resultado}")
    elif opcion == 4:
        resultado = nro1 / nro2
        print(f"EL resultado de la operacion (Division) es {resultado}")
    elif opcion == 0:
        print("No elegiste usar la calculadora, Adios")
    else:
        print("ERROR te pedi opciones del 0 al 4")
    # endif
# end while




