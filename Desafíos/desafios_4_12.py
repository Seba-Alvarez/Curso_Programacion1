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
    
#el menu este se lo pedi a chatgpt usando de base uno que hice hace un tiempo, no queria escribirlo otra vez a mano jaja

def menu_autores_libros():
    gestion_libros = GestionLibro()  # Incluye internamente una instancia de GestionAutores
    gestion_autores = gestion_libros.gestion_autores  # Acceso directo a autores

    while True:
        print("\n--- MENÚ GESTIÓN AUTORES Y LIBROS ---")
        print("1. Alta Autor")
        print("2. Baja Autor")
        print("3. Mostrar Autores")
        print("4. Buscar Autor")
        print("5. Alta Libro")
        print("6. Baja Libro")
        print("7. Mostrar Libros")
        print("8. Buscar Libro")
        print("9. Salir")

        opcion = input("Seleccione una opción (1-9): ")

        if opcion == "1":
            print("\n-- Alta de Autor --")
            nombre = input("Nombre del autor: ")
            fecha_nac = input("Fecha de nacimiento: ")
            nacionalidad = input("Nacionalidad: ")
            gestion_autores.alta_autor(nombre, fecha_nac, nacionalidad)

        elif opcion == "2":
            print("\n-- Baja de Autor --")
            nombre = input("Nombre del autor a eliminar: ")
            autor = gestion_autores.buscar_autor(nombre)
            if autor:
                gestion_autores.baja_autor(autor)

        elif opcion == "3":
            print("\n-- Mostrar Autores --")
            gestion_autores.mostrar_autores()

        elif opcion == "4":
            print("\n-- Buscar Autor --")
            nombre = input("Nombre del autor a buscar: ")
            gestion_autores.buscar_autor(nombre)

        elif opcion == "5":
            print("\n-- Alta de Libro --")
            nombre_autor = input("Nombre del autor del libro: ")
            autor = gestion_autores.buscar_autor(nombre_autor)
            if autor:
                titulo = input("Título del libro: ")
                genero = input("Género: ")
                isbn = input("ISBN: ")
                gestion_libros.alta_libro(autor, titulo, genero, isbn)

        elif opcion == "6":
            print("\n-- Baja de Libro --")
            titulo = input("Título del libro a eliminar: ")
            libro = gestion_libros.buscar_libro(titulo)
            if libro:
                gestion_libros.baja_libro(libro)

        elif opcion == "7":
            print("\n-- Mostrar Libros --")
            gestion_libros.mostrar_libros()

        elif opcion == "8":
            print("\n-- Buscar Libro --")
            titulo = input("Título del libro a buscar: ")
            gestion_libros.buscar_libro(titulo)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Ingrese un número del 1 al 9.")

if __name__ == "__main__":
    menu_autores_libros()
