from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import  CatalogoPeliculas as catalogo
opcion = None
while opcion != 4:
    try:
        print('opciones')
        print('1. Agregar Peliculas')
        print('2. Listar Peliculas')
        print('3. Eliminar Peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporcionaa el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregarPelicula(pelicula)
        elif opcion == 2:
            catalogo.listarPeliculas()
        elif opcion == 3:
            catalogo.eliminarPeliculas()

    except Exception as e:
        print(f'Ha ocurrido un error {e}')
        opcion = None
else:
    print('Salimos del programa...')
