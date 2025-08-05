#Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
# Proporciona métodos getter y setter para cada atributo.

#clase libro con atributos privados, con __ antes del atributo, si tiene un _ sería protegido
class Libro:
    #constructor con los atributos
    def __init__(self, titulo, autor, isbn):
        #aca se definen como privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    #propery es un decorador que esta convirtiendo al metodo en un getter, 
    # esto permite permite acceder a un atributo 
    # como si fuera una propiedad, aunque sea un método.
    #un getter es un metodo que obtiene el valor de un atributo.
    @property
    #esto solo también es un getter, pero con property se genera una interfaz mas limpia
    def titulo(self):
        return self.__titulo

    #<metodo>.setter es tambien un decorador, pero este esta convirtiendo al metodo en un setter,
    #es decir, permite modificarlo, controlando dichas modificaciones
    #un setter es un metodo que que cambia el valor de un atributo
    #gracias al decorador setter, se puede instanciar al objeto.atributo = "nuevo" para modificar el atributo
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    #lo mismo que el getter de titulo pero con autor
    @property
    def autor(self):
        return self.__autor

    #lo mismo que el setter titulo pero con autor
    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    #lo mismo que el getter autor y titulo pero con isbn
    @property
    def isbn(self):
        return self.__isbn

    #este setter es tecnicamente igual en la medida que también convierte al metodo en un setter,
    #es decir, que permite la modificacion del atributo, pero aca se esta haciendo 
    #una validación que los isbn solo pueden ser cadenas de texto
    #si al modificar el atributo se le pasa otro tipo de dato va a tirar error con raise ValueError
    @isbn.setter
    def isbn(self, nuevo_isbn):
        if isinstance(nuevo_isbn, str):
            self.__isbn = nuevo_isbn
        else:
            raise ValueError("El ISBN debe ser una cadena de texto.")

#Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. 
# Proporciona un método para agregar libros a esta lista.

"""

#clase con atributos privados
class Autor:
    #constructor con los atributos de la clase
    def __init__(self, nombre, nacionalidad):
        #atrbutos privados, es decir con __
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        #lista de libros, también privada
        self.__libros = []

    #getter de nombre
    def get_nombre(self):
        return self.__nombre

    #setter de nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    #getter de nacionalida
    def get_nacionalidad(self):
        return self.__nacionalidad

    #setter de nacionalidad
    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad
    
    #alta libro, aca se esta chequeando si se le esta pasando un objeto libro
    def alta_libro(self, libro):
        #si es un objeto libro
        if isinstance(libro, Libro):
            #se agrega a la lista de libros
            #hay que instanciarla con self porque es un atributo de una clase
            self.__libros.append(libro)
        else:
            #si no es un objeto libro tira un error
            raise TypeError("Solo se pueden agregar objetos de tipo Libro")

    #un mostrar libros muy basico
    def get_libros(self):
        return self.__libros

"""

#Implementa la clase Autor con métodos getter y setter utilizando decoradores @property 
# para manejar los atributos privados nombre y nacionalidad.

#clase con atributos privados
class Autor:
    #constructor con los atributos de la clase
    def __init__(self, nombre, nacionalidad):
        #atrbutos privados, es decir con __
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        #lista de libros, tambien privada
        self.__libros = []

    #propery es un decorador que esta convirtiendo al metodo en un getter, 
    # esto permite permite acceder a un atributo 
    # como si fuera una propiedad, aunque sea un método.
    #un getter es un metodo que obtiene el valor de un atributo.
    @property
    #esto solo también es un getter, pero con property se genera una interfaz mas limpia
    def nombre(self):
        return self.__nombre

    #<metodo>.setter es tambien un decorador, pero este esta convirtiendo al metodo en un setter,
    #es decir, permite modificarlo, controlando dichas modificaciones
    #un setter es un metodo que que cambia el valor de un atributo
    #gracias al decorador setter, se puede instanciar al objeto.atributo = "nuevo" para modificar el atributo
    def nombre(self, nombre):
        self.__nombre = nombre

    #lo mismo que el getter de nombre
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    #lo mismo que el setter de nombre
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    #alta libro, aca se esta chequeando si se le esta pasando un objeto libro
    def alta_libro(self, libro):
        #si es un objeto libro
        if isinstance(libro, Libro):
            #se agrega a la lista de libros
            #hay que instanciarla con self porque es un atributo de una clase
            self.__libros.append(libro)
        else:
            #si no es un objeto libro tira un error
            raise TypeError("Solo se pueden agregar objetos de tipo Libro")

    #un mostrar libros muy basico
    def get_libros(self):
        return self.__libros

#Crea una función que tome un objeto Autor y 
# devuelva una lista de todos los títulos de libros escritos por el autor. 
# Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor.

#funcion para obtener libros, esto tiene que tener al menos un atributo titulo que sea publico, porque sino,
#al estar fuera de la clase no va a poder acceder a los atributos privados
#siendo que no se esta modificando nada, no se pueden usar setters para hacerlo
#se le pasa un parametro autor, que es una instancia de la clase Autor
def obtener_titulos_autor(autor):
    #si no se le pasa un objeto autor va a tirar un error
    if not isinstance(autor, Autor):
        raise TypeError("Se esperaba un objeto de tipo Autor")
    #si efectivamente se le pasa un objeto autor, recorre la lista de libros y los muestra con return (en forma de lista)
    #esto necesita algun metodo publico para acceder a la lista, porque la lista en si es privada
    return [libro.titulo for libro in autor.get_libros()]

#desarrolla una funcion que reciba una lista de objetos Autor y 
#devuelva el autor que ha escrito el mayor número de libros 
#utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.

#funcion que recibe una lista de autores y devuelve el que tiene mas libros
def autor_con_mas_libros(lista_autores):
    # si la lista esta vacia, devuelve None
    if not lista_autores:
        return None

    #se chequea que todos los elementos de la lista sean objetos de tipo autor,
    #si alguno no lo es levanta un error
    if not all(isinstance(autor, Autor) for autor in lista_autores):
        raise TypeError("Todos los elementos deben ser objetos de tipo Autor")

    #se usa max para encontrar el autor que tiene mas libros
    #se usa una lambda para contar la cantidad de libros que tiene cada autor usando el metodo publico get_libros()
    #por lo cual es un correcto uso del encapsulamiento, pues no esta accediendo directamente a __libros, sino que esta
    #usando el metodo publico get_libros
    return max(lista_autores, key=lambda autor: len(autor.get_libros()))
