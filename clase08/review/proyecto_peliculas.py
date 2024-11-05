'''
Una película

[titulo(str), duracion(int en minutos), calificacion(float)]

'''

# peliculas = []
peliculas = [
    ["Inception", 148, 8.8],
    ["The Matrix", 136, 8.7],
    ["Interstellar", 169, 8.6],
    ["The Godfather", 175, 9.2],
    ["The Dark Knight", 152, 9.0],
    ["Pulp Fiction", 154, 8.9],
    ["Forrest Gump", 142, 8.8],
    ["Fight Club", 139, 8.8],
    ["The Shawshank Redemption", 142, 9.3]   
]

while True:
    print("*" * 20)
    print("Menu De Opciones\n")
    print("1. Agregar Película ")
    print("2. Mostrar Todas ")
    print("3. MostrarLas mejores ")
    print("0. Salir ")
    print("*" * 20)

    opcion = input("Ingresa una opcion: ") 
    opcion = int(opcion)

    if opcion == 0:
        print("Nos vemos !!!")
        break
    elif opcion == 1:
        print("Alta de Película")

        titulo = input("Título de la película: ")
        duracion = int(input("Duración en minutos: "))
        calificacion = float(input("Calificación: "))

        # Armamos la película ingresada
        pelicula = [titulo, duracion, calificacion]
        # Agregar la película al listado
        peliculas.append(pelicula)
    elif opcion == 2:
        print("Listado")
        if len(peliculas) == 0:
            print("Aún no tenemos películas cargadas en el sistema")
        else:
            print("titulo".ljust(30) + "duracion".ljust(10) + "calificacion" + " Comentario")
            for pelicula in peliculas:
                comentario = ""
                if pelicula[2] >= 9.0:
                    comentario = "EXCELENTE"
                elif pelicula[2] >= 7.0:
                    comentario = "BUENA"
                elif pelicula[2] < 7.0:
                    comentario = "REGULAR"
                print(f"{pelicula[0].ljust(30)}{str(pelicula[1]).ljust(10)}{pelicula[2]} {comentario}")
    elif opcion == 3:
        print("Listado de Excelentes")
        if len(peliculas) == 0:
            print("Aún no tenemos películas cargadas en el sistema")
        else:
            print("titulo".ljust(30) +  " Comentario")
            for pelicula in peliculas:
                if pelicula[2] >= 9:
                    print(f"{pelicula[0].ljust(30)}")
    else:
        print("Por favor, ingresa una opción válida")

print("FIN DEL PROGRAMA")
