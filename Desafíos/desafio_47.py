class Autor:
    #se definen los atributos con el constructor
    def __init__(self, nombre = "", nacionalidad = ""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        #se crea un lista de libros (que es también un atributo de la clase)
        self.lista_libros = []

    #métodos de la clase, alta, baja y mostrar. Se muestran los autores y los libros
    def alta_libro(self, libro):
        self.lista_libros.append(libro)

    def baja_libro(self, libro):
        originales = len(self.lista_libros)
        self.lista_libros = [l for l in self.lista_libros if l != libro]
        if len(self.lista_libros) < originales:
            print(f"Libro(s) '{libro}' eliminado(s).")
        else:
            print(f"Libro '{libro}' no encontrado.")

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

    def mostrar_libros(self):
        if not self.lista_libros:
            print("No hay libros")
        else:
            print("Libros:")
            for libro in self.lista_libros:
                print(libro)
