#Implementa una clase Poeta que herede de Autor y 
# tenga un atributo para el tipo de poesía que escribe.

#se crea la clase padre
class Autor:
    #se crea el constructor con los atributos de la clase padre
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    #el metodo str define como se representa la informacion guardada en los atributos, en este caso es un texto
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

#clase hija, que hereda los atributos y metodos de autor
class Poeta(Autor):
    #constructor con los datos de la clase padre y la clase hija
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        #aca se esta usando super para llamar al constructor (con los atributos) de la clase padre para no repetir codigo
        super().__init__(nombre, nacionalidad)
        #ademas se agrega el nuevo atributo de esta clase
        self.tipo_poesia = tipo_poesia

    #aca se esta redefiniendo el metodo str para mostrar también los datos de la clase poeta
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad}) - Poesía: {self.tipo_poesia}"


#Crea una clase Bibliotecario que herede de Usuario y 
# tenga atributos específicos como sección y años_experiencia.

#clase padre
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #metodo para mostrar la información que tienen los atributos de la clase, se le pasa la instancia de la clase para
    #que pueda acceder a los atributos. estos estan formateados como f-strings
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

#clase hija que hereda los atributos y metodos de usuario
class Bibliotecario(Usuario):
    #se incializa el constructor con la instancia a la clase, los atributos de la clase padre y los nuevos de la clase hija
    def __init__(self, nombre, edad, seccion, años_experiencia):
        #con super se llama al constructor del usuario que ya contiene los atributos
        super().__init__(nombre, edad)
        #estos son los atributos nuevos
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    #se esta sobrescribiendo el metodo mostrar_info de la clase padre para mostrar la informacion completa de la clase hija
    #esto se llama polimorfismo
    def mostrar_info(self):
        #con super se llama al metodo original
        super().mostrar_info()
        #despues se agregan los datos nuevos
        print(f"Sección: {self.seccion}")
        print(f"Años de experiencia: {self.años_experiencia}")


#Diseña una clase LibroDigital que herede de Libro y añada atributos como formato 
# (e.g., PDF, EPUB) y tamaño_archivo. 
# Además, implementa una subclase EBook que sobrescriba un método para 
# mostrar información específica, como enlaces de descarga.

#clase padre
class Libro:
    #constructor con la instancia y los atributos de la clase
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    #metodo para mostrar la información, se le pasa la instancia de la clase para que pueda acceder a los atributos
    def mostrar_info(self):
        #se muestran los atributos de la clase
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.año_publicacion}")

#clase hija que hereda de libro
class LibroDigital(Libro):
    #se incializa el constructor con la instancia y los datos de la clase padre e hija
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo):
        #super llama al constructor y los metodos originales
        super().__init__(titulo, autor, año_publicacion)
        #se agregan los nuevos atributos de la clase
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    #aca se esta sobrescribiendo el metodo mostrar info para mostrar los datos actualizados
    def mostrar_info(self):
        #con super se esta llamando al mostrar info original
        super().mostrar_info()
        #ademas se agregan los otros atributos
        print(f"Formato: {self.formato}")
        print(f"Tamaño del archivo: {self.tamaño_archivo} MB")

#se crea una clase hija de libro digital
class EBook(LibroDigital):
    #se inicializa el constructor con los datos de la clase padre (libro digital) y de su clase padre (libro)
    #se le tienen que pasar todos los datos de su clase padre y como libro digital esta heredando de libro
    #hay que agregar los atributos al constructor
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño_archivo, enlace_descarga):
        #con super se llama a los atributos de libro digital (que a su vez esta 
        # usando super para llamar a los de su clase padre)
        super().__init__(titulo, autor, año_publicacion, formato, tamaño_archivo)
        #se agregan los nuevos atributos
        self.enlace_descarga = enlace_descarga

    #otra vez se sobrescribe el metodo de mostrar la info para agregar los atributos de ebook
    def mostrar_info(self):
        #con super se llama al mostrar info de libro digital, que a su vez esta llamando al mostrar info original
        super().mostrar_info()
        #se muestra el nuevo atributo
        print(f"Enlace de descarga: {self.enlace_descarga}")


#Implementa una clase EscritorAcademico que herede de Escritor y Academico, 
# e incluya un método adicional para publicar artículos académicos. 
# Asegúrate de utilizar correctamente la función super() para inicializar las clases base.

#clase padre de escritoracademico
class Escritor:
    #se inicializa el constructor con los atributos de la clase
    #kwargs significa keybord arguments, esto es una forma de pasar una cantida variable de  
    # parametros con nombre a una función o método
    # ** es un operador de desempaquetado que convierte los argumentos en forma de 
    # diccionario cuando los pasás o recibís en una función.
    #es decir, se estan pasando los atributos en forma de diccionario hasta llegar a la clase hija
    def __init__(self, nombre, genero, **kwargs):
        #aca no se esta llamando a una clase padre, sino que se llama al siguiente constructor
        #esto es por como python busca los metodos cuando hay herencia multiple
        #va a ir de arriba hacia abajo, este super esta llamando al siguiente constructor (el de academico)
        super().__init__(**kwargs)
        #se asignan los atributos
        self.nombre = nombre
        self.genero = genero

    #metodo para mostrar los atributos de la clase
    def escribir(self):
        print(f"{self.nombre} está escribiendo en el género {self.genero}.")

#clase padre de escritoracademico (igual que arriba)
class Academico:
    #lo mismo que escritor
    def __init__(self, universidad, area_investigacion, **kwargs):
        #igual que arriba, pero este esta llamando al siguiente constructor en el orden (el de la clase hija)
        super().__init__(**kwargs)
        self.universidad = universidad
        self.area_investigacion = area_investigacion

    #metodo distinto para mostrar los atributos de la clase, pero estan haciendo lo mismo
    def investigar(self):
        print(f"Investigando en el área de {self.area_investigacion} en {self.universidad}.")

#clase hija que hereda de escritor y academico
class EscritorAcademico(Escritor, Academico):
    #constructor con los atributos de las clases padre y su hija
    #aca no hay que pasarle kwargs porque se estan usando los atributos de ambas clases padre
    #kwargs cumplio su funcion pasando los atributos y metodos de ambas clases padre a la clase hija
    def __init__(self, nombre, genero, universidad, area_investigacion):
        #con super se llaman a los atributos de ambas clases padre
        #si no se hubiera usado kwargs, usar super solo hubiera traido los atributos y metodos de la primera clase padre
        #ignorando a la segunda, esto por el orden que python busca
        #porque kwargs esta pasando un diccionario (no tiene orden), hay que asignar 
        # los atributos con los argumentos que va a recibir
        super().__init__(nombre=nombre, genero=genero, universidad=universidad, area_investigacion=area_investigacion)

    #metodo para publicar articulos academicos como pide la letra
    #lo unico que hay que pasarle es el titulo del articulo, que no es un atributo sino un argumento
    def publicar_articulo(self, titulo_articulo):
        print(f"{self.nombre} ha publicado un artículo academico titulado '{titulo_articulo}' en el area de {self.area_investigacion}.")

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
