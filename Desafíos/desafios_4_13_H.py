#Implementa una clase Poeta que herede de Autor y 
# tenga un atributo para el tipo de poesía que escribe.

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad}) - Poesía: {self.tipo_poesia}"


#Crea una clase Bibliotecario que herede de Usuario y 
# tenga atributos específicos como sección y años_experiencia.

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Bibliotecario(Usuario):
    def __init__(self, nombre, edad, seccion, años_experiencia):
        super().__init__(nombre, edad)  # Llama al constructor de Usuario
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sección: {self.seccion}")
        print(f"Años de experiencia: {self.años_experiencia}")


#Diseña una clase LibroDigital que herede de Libro y añada atributos como formato 
# (e.g., PDF, EPUB) y tamaño_archivo. 
# Además, implementa una subclase EBook que sobrescriba un método para 
# mostrar información específica, como enlaces de descarga.

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo):
        super().__init__(titulo, autor, año_publicacion)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato: {self.formato}")
        print(f"Tamaño del archivo: {self.tamaño_archivo} MB")

class EBook(LibroDigital):
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, año_publicacion, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Enlace de descarga: {self.enlace_descarga}")


#Implementa una clase EscritorAcademico que herede de Escritor y Academico, 
# e incluya un método adicional para publicar artículos académicos. 
# Asegúrate de utilizar correctamente la función super() para inicializar las clases base.

class Escritor:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def escribir(self):
        print(f"{self.nombre} está escribiendo en el género {self.genero}.")

class Academico:
    def __init__(self, universidad, area_investigacion):
        self.universidad = universidad
        self.area_investigacion = area_investigacion

    def investigar(self):
        print(f"Investigando en el área de {self.area_investigacion} en {self.universidad}.")

class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad, area_investigacion):
        super().__init__(nombre, genero)
        Academico.__init__(self, universidad, area_investigacion)

    def publicar_articulo(self, titulo_articulo):
        print(f"{self.nombre} ha publicado un artículo académico titulado '{titulo_articulo}' en el área de {self.area_investigacion}.")

#Crea una jerarquía de clases para representar diferentes tipos de empleados en una biblioteca, 
# utilizando herencia múltiple y composición. 
# Por ejemplo, implementa clases como Empleado, Gerente, Tecnico, y Voluntario, 
# donde Gerente y Tecnico hereden de Empleado, y algunos puedan tener roles adicionales 
# mediante composición con otras clases como Administrador o Mantenimiento.

class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def trabajar(self):
        print(f"{self.nombre} está trabajando como empleado.")

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, departamento):
        super().__init__(nombre, id_empleado)
        self.departamento = departamento

    def dirigir(self):
        print(f"{self.nombre} está dirigiendo el departamento de {self.departamento}.")

class Tecnico(Empleado):
    def __init__(self, nombre, id_empleado, especialidad):
        super().__init__(nombre, id_empleado)
        self.especialidad = especialidad

    def reparar(self):
        print(f"{self.nombre} está reparando equipos de {self.especialidad}.")

class Voluntario:
    def __init__(self, nombre, area_asignada):
        self.nombre = nombre
        self.area_asignada = area_asignada

    def ayudar(self):
        print(f"{self.nombre} está ayudando en el área de {self.area_asignada} como voluntario.")

class Administrador:
    def __init__(self, nivel_admin):
        self.nivel_admin = nivel_admin

    def administrar(self):
        print(f"Administrando con nivel {self.nivel_admin}.")

class Mantenimiento:
    def __init__(self, herramientas):
        self.herramientas = herramientas

    def mantener(self):
        print(f"Mantenimiento usando herramientas: {', '.join(self.herramientas)}.")

class GerenteAdministrador(Gerente):
    def __init__(self, nombre, id_empleado, departamento, nivel_admin):
        super().__init__(nombre, id_empleado, departamento)
        self.administrador = Administrador(nivel_admin)

    def administrar(self):
        self.administrador.administrar()

class TecnicoMantenimiento(Tecnico):
    def __init__(self, nombre, id_empleado, especialidad, herramientas):
        super().__init__(nombre, id_empleado, especialidad)
        self.mantenimiento = Mantenimiento(herramientas)

    def mantener(self):
        self.mantenimiento.mantener()
