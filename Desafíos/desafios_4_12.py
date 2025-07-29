#se crea la clase autor
class Autor:
    #costructor con los atributos
    def __init__(self, nombre, fecha_nac, nacionalidad):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.nacionalidad = nacionalidad
        #lista de libros para asociar los autores a los libros
        self.lista_libros = []

    #metodo para agregar libros, este los está asociando con los autores
    def alta_libro(self, libro):
        self.lista_libros.append(libro)

    #metodo para mostrar la salida de los datos de forma controlada (en un string en este caso)
    def __str__(self):
        return f"Nombre {self.nombre}, Fecha de Nacimiento {self.fecha_nac}, Nacionalidad {self.nacionalidad}"
    
#se crea la clase Libro
class Libro:
    #constructor con los datos del libro + el autor asociado
    def __init__(self, autor, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        #tiene que haber un autor primero antes de agregar el libro
        #medio como en la vida real, no hay libro sin autor jaja
        self.autor = autor
        #se llama al metodo alta_libro del objeto autor, no al de la clase gestion
        autor.alta_libro(self)

    #lo mismo que arriba
    def __str__(self):
        return f"Titulo {self.titulo}, Genero {self.genero}, ISBN {self.isbn}, Autor {self.autor.nombre}"

#clase que tiene la gestion de autores
class GestionAutores:
    def __init__(self):
        #lista de autores
        self.autores = []

    #se agregan los autores a la lista, ya con los parametros de la clase
    def alta_autor(self, nombre, fecha_nac, nacionalidad):
        #se verifica que los parametros que se le van a pasar despues sean correctos
        #es decir, que se le pase un nombre, una fecha de nacimiento y una nacionalidad
        if not nombre or not fecha_nac or not nacionalidad:
            print("Datos incompletos")
            #devuelve None y no crea el autor
            return None

        #se guardan los datos ingresados en una variable
        nuevo_autor = Autor(nombre, fecha_nac, nacionalidad)
        #ahora si se agrega el autor a la lista con el append, se le pasan los datos guardados en la variable
        self.autores.append(nuevo_autor)
        #se retorna un objeto, que es el nuevo autor agregado
        return nuevo_autor


    #aca no se necesita corroborar si los datos son correctos
    def baja_autor(self, autor):
        #se corrobora si el autor en cuestion existe en la lista
        if autor in self.autores:
            self.autores.remove(autor)
        else:
            print("Autor no encontrado") 

    #se muestran los autores, un listar de toda la vida
    def mostrar_autores(self):
        if not self.autores:
            print("No hay autores")
        else:
            print("Autores:")
            for autor in self.autores:
                print(autor)

    #una busqueda de autores por nombre
    def buscar_autor(self, nombre):
        #se recorren los autores
        for autor in self.autores:
            #si existe un autor con el nombre ingresado se retorna el objeto autor
            if autor.nombre.lower() == nombre.lower():
                print(f"Autor encontrado: {autor}")
                return autor
        #esto esta afuera del bucle para que pase solo si no se encuentran los autores
        print(f"No se encontro el autor {nombre}")
        return None

#todo lo mismo menos el alta_libro que se le agrega una validación para 
# asegurarse que primero haya un autor y despues un libro (como en la vida real jaja)
class GestionLibro:
    def __init__(self):
        self.libros = []
        #relación con gestion de autores para ingresar libros con autores validos
        #aca se esta asignando la clase 
        self.gestion_autores = GestionAutores()

    def alta_libro(self, autor, titulo, genero, isbn):
        #aca se esta verificando si el autor del libro existe en la clase de gestion
        if autor not in self.gestion_autores.autores:
            #si no esta registrado retorna None
            print(f"Error: el autor '{autor.nombre}' no está registrado. No se puede crear el libro.")
            return None

        #Si esta registrado, se crea el libro y se agrega a la lista de libros
        #esto es igual que el alta_autor pero con libro
        libro = Libro(autor, titulo, genero, isbn)
        self.libros.append(libro)
        return libro

    #el resto es lo mismo pero para libros en vez de autores
    def baja_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print("Libro no encontrado") 

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros")
        else:
            print("Libros:")
            for libro in self.libros:
                print(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(f"Libro encontrado: {libro}")
                return libro
        print(f"No se encontro el libro {titulo}")
        return None