from dominio.pelicula import Pelicula
from servicios.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None

while opcion != '4':
    try:
        print('opciones')
        print('1. agregar peliculas')
        print('2. listar peliculas')
        print('3. eliminar archivo de peliculas')
        print('4. salir')
        opcion = input('escribe tu opción (1-4): ')
        if opcion == '1':
            nombre_pelicula = input('Escribe el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == '2':
            cp.listar_peliculas()
        elif opcion == '3':
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None

print('Salimos del programa...')

