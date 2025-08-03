#Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
# Proporciona métodos getter y setter para cada atributo.

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, nuevo_isbn):
        if isinstance(nuevo_isbn, str):
            self.__isbn = nuevo_isbn
        else:
            raise ValueError("El ISBN debe ser una cadena de texto.")

#Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. 
# Proporciona un método para agregar libros a esta lista.

"""

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
    
    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.__libros.append(libro)
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Libro")

    def get_libros(self):
        return self.__libros

"""

#Implementa la clase Autor con métodos getter y setter utilizando decoradores @property 
# para manejar los atributos privados nombre y nacionalidad.

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.__libros.append(libro)
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Libro")

    def get_libros(self):
        return self.__libros

#Crea una función que tome un objeto Autor y 
# devuelva una lista de todos los títulos de libros escritos por el autor. 
# Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor.

def obtener_titulos_autor(autor):
    if not isinstance(autor, Autor):
        raise TypeError("Se esperaba un objeto de tipo Autor")
    
    return [libro.titulo for libro in autor.get_libros()]

#Desarrolla una función que reciba una lista de objetos Autor y 
# devuelva el autor que ha escrito el mayor número de libros. 
# Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.

def autor_con_mas_libros(lista_autores):
    if not lista_autores:
        return None  # O lanzar una excepción si prefieres
    
    if not all(isinstance(autor, Autor) for autor in lista_autores):
        raise TypeError("Todos los elementos deben ser objetos de tipo Autor")

    return max(lista_autores, key=lambda autor: len(autor.get_libros()))
