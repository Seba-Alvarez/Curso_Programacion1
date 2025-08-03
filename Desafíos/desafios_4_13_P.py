
#Crea una clase Musico que tenga un método instrumento y crea dos subclases 
#Guitarrista y Baterista que sobrescriban el método instrumento. 
#Instancia objetos de estas clases y demuestra el polimorfismo.

class Musico:
    def instrumento(self):
        return "Instrumento genérico"

class Guitarrista(Musico):
    def instrumento(self):
        return "Guitarra"

class Baterista(Musico):
    def instrumento(self):
        return "Batería"

musico = Musico()
guitarrista = Guitarrista()
baterista = Baterista()

for m in (musico, guitarrista, baterista):
    print(f"{m.__class__.__name__} toca {m.instrumento()}")


#Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor. 
# Instancia un objeto de la clase Escritor y muestra 
# cómo se puede acceder al método biografia de ambas clases.

class Autor:
    def biografia(self):
        return "Biografía genérica del autor."

class Escritor(Autor):
    def biografia(self):
        return "Biografía específica del escritor."

    def biografia_autor(self):
        return super().biografia()

escritor = Escritor()

print("Biografia del Escritor:", escritor.biografia())
print("Biografia del Autor desde Escritor:", escritor.biografia_autor())


#En este desafío, vamos a extender la clase Libro para crear una subclase `LibroEspecializado`. 
# Un `LibroEspecializado`, además de tener un título y un autor, 
# también tiene un campo de estudio y un nivel de especialización (básico, intermedio, avanzado).

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"'{self.titulo}' escrito por {self.autor}"

class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion

    def descripcion(self):
        return (f"'{self.titulo}' escrito por {self.autor}, "
                f"campo: {self.campo_estudio}, nivel: {self.nivel_especializacion}")

#En este desafío, se te pide que implementes el polimorfismo con métodos de clase 
# en figuras geométricas. Deberás crear una clase base Figura 
# con un método area y dos subclases Circulo y Cuadrado que sobrescriban 
# este método para calcular el área de cada figura.

import math

class Figura:
    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

#En este desafío, aplicarás el polimorfismo para realizar diferentes operaciones matemáticas. 
# Deberás crear una clase base Operacion con un método resultado y dos subclases 
# Suma y Multiplicacion que sobrescriban este método para realizar las operaciones correspondientes.

class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultado(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Suma(Operacion):
    def resultado(self):
        return self.a + self.b

class Multiplicacion(Operacion):
    def resultado(self):
        return self.a * self.b
