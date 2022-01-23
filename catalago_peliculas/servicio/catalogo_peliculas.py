import os


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f'{ pelicula.nombre } \n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.ruta_archivo,'r',encoding='utf-8') as archivo:
            print('Catalogo de Peliculas '.center(50,'-',))
            print(archivo.read())
    @classmethod
    def eliminarPeliculas(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo elimnado: { cls.ruta_archivo}')