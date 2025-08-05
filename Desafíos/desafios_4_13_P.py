
#Crea una clase Musico que tenga un método instrumento y crea dos subclases 
#Guitarrista y Baterista que sobrescriban el método instrumento. 
#Instancia objetos de estas clases y demuestra el polimorfismo.

#Polimorfismo permite usar el mismo método en diferentes objetos, pero con comportamientos específicos de cada uno.
#se crea la clase base con un metodo instrumento
class Musico:
    def instrumento(self):
        return "Instrumento genérico"

#se definen las clases derivadas que van a heredar el metodo instrumento
#cada clase sobrescribe el metodo con un instrumento diferente
class Guitarrista(Musico):
    def instrumento(self):
        return "Guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "Batería"

#se crean las instancias de cada clase para poder mostrar cada instrumento
#y se guardan en variables
musico = Musico()
guitarrista = Guitarrista()
baterista = Baterista()

#aca se recorren los tres métodos y se llama al método instrumento, pero al sobrescribirlo
#cada método va a mostrar un instrumento distinto
for m in (musico, guitarrista, baterista):
    print(f"{m.__class__.__name__} toca {m.instrumento()}")
#esto va a mostrar:
#Musico toca Instrumento generico
#Guitarrista toca Guitarra
#Baterista toca Bateria


#Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor. 
# Instancia un objeto de la clase Escritor y muestra 
# cómo se puede acceder al método biografia de ambas clases.

#clase base
class Autor:
    def biografia(self):
        return "Biografía genérica del autor."

#aca se crea una subclase que sobrescribe el método biografia para mostrar biografias especificas
class Escritor(Autor):
    def biografia(self):
        return "Biografía específica del escritor."

    #super es una funcion se usa para llamar metodos de una clase padre desde una clase base/hija
    #aca se esta llamando al método de Autor, no de escritor (usando super)
    def biografia_autor(self):
        return super().biografia()

#aca se instancia un objeto tipo escritor
escritor = Escritor()

#aca se esta llamando al metodo sobreescrito de la clase escritor, que va a mostrar biografia especificas
print("Biografia del Escritor:", escritor.biografia())
#aca se esta llamando al metodo de la clase escritor, que a su vez esta usando super para llamar al
#metodo de autor (al original de la clase base)
#esto va a mostrar biografia generica
print("Biografia del Autor desde Escritor:", escritor.biografia_autor())


#En este desafío, vamos a extender la clase Libro para crear una subclase `LibroEspecializado`. 
# Un `LibroEspecializado`, además de tener un título y un autor, 
# también tiene un campo de estudio y un nivel de especialización (básico, intermedio, avanzado).

#clase base
class Libro:
    #se incializa el constructor con dos atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    #metodo que devuelve un string con info del libro
    def descripcion(self):
        return f"'{self.titulo}' escrito por {self.autor}"

#clase que hereda de libro que añade dos atributos campo estudio y especializacion
#se inicializa el constructor con los atributos de la clase, pero se asignan los atributos solo de esta clase
#esto es por herencia, los otros dos métodos los está sacando de la clase libro
#ademas se esta usando un constructor que llama con super a los atributos de la clase libro para reusar la inicializacion
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    #aca se sobrescribe el metodo descripcion de la clase padre para cambiar la descripcion y agregar mas detalles
    def descripcion(self):
        return (f"'{self.titulo}' escrito por {self.autor}, "
                f"campo: {self.campo_estudio}, nivel: {self.nivel_especializacion}")

#En este desafío, se te pide que implementes el polimorfismo con métodos de clase 
# en figuras geométricas. Deberás crear una clase base Figura 
# con un método area y dos subclases Circulo y Cuadrado que sobrescriban 
# este método para calcular el área de cada figura.

#se importa math para usar pi
import math

#clase base con un metodo que lanza una excepcion si no se lo sobrescribe
#esto para forzar a las otras clases a definir su propia implementacion de area
#esto es un método abstracto, es decir, un metodo que se declara pero no se implementa en la clase base
#se usa cuando la clase base necesita de sus clases hijas para tener sentido, como en este caso,
#para calcular areas de diferentes figuras se necesitan diferentes datos
class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

#circulo hereda de figura
class Circulo(Figura):
    #se incializa el constructor con el radio
    def __init__(self, radio):
        self.radio = radio

    #aca se calcula el radio sobrescribiendo el metodo area de figura, los calculos usando pi de math 
    # e instanciando el radio
    def area(self):
        return math.pi * self.radio ** 2

#tambien hereda de figura
class Cuadrado(Figura):
    #aca se incializa el lado
    def __init__(self, lado):
        self.lado = lado

    #se sobrescribe area y se instancia el atributo lado
    def area(self):
        return self.lado ** 2

#En este desafío, aplicarás el polimorfismo para realizar diferentes operaciones matemáticas. 
# Deberás crear una clase base Operacion con un método resultado y dos subclases 
# Suma y Multiplicacion que sobrescriban este método para realizar las operaciones correspondientes.

#clase base con dos atributos para hacer operaciones
class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #clase abstracta que obliga a las subclases a implementar diferentes metodos para cada operacion
    def resultado(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

#clase suma, que hereda de operacion (los atributos) y sobrescribe el metodo resultado para hacer sumas
class Suma(Operacion):
    def resultado(self):
        return self.a + self.b

#clase multiplicacion, que hereda de operacion (los atributos) y sobrescribe el metodo resultado para hacer multiplicaciones
class Multiplicacion(Operacion):
    def resultado(self):
        return self.a * self.b
