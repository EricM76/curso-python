

lista = [2, 5, 7 , 5, 9]




for elemento in lista :
    if elemento % 2 == 0:
        res = elemento * 2
    else:
        res = elemento + 9
    print(res)


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

for pelicula in peliculas:
    if pelicula[1] > 150 and pelicula[2] >= 9:
        print(pelicula[0].upper())