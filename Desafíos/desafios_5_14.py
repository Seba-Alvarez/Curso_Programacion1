#Desafío 67: 
#Solicita al usuario dos números enteros e implementa un try-except que maneje la división por cero y }
#los valores no numéricos. Muestra mensajes de error apropiados en cada caso.
try:
    #aca ya se está limitando a que se ingrese un integer
    num1 = int(input("Ingresar numero entero: "))
    num2 = int(input("Ingresar numero entero: "))
    #aca se hace el resultado
    resultado = num1 / num2
    #se imprime por pantalla
    print(f"Resultado: {resultado} ")
#excepcion para cuando se ingresa 0, porque no se puede dividir por 0
except ZeroDivisionError:
    print("Ingresar algun numero que no sea cero.")
#error por si no se ingresa un número entero
except ValueError:
    print("Por favor ingresar un numero entero")

#Desafío 68: 
#Crea un programa que tome una lista de valores y realice operaciones matemáticas sobre ellos. 
# Implementa el manejo de varias excepciones comunes como ZeroDivisionError, TypeError, y ValueError.

#aca una lista para hacer operaciones, que va a tirar distintos errores
valores = [10, 5, 0, 'a', 3]

#for para recorrer todos los elementos de la lista
for valor in valores:
    #aca es la operación que va a hacer
    try:
        #se va a dividir 100 entre 10, 5, 0, 'a' y 3
        resultado = 100 / int(valor)
        #se muestra el resultado por pantalla
        print("Resultado: {resultado} ")
    #excepcion para el 0
    except ZeroDivisionError:
        #se muestra el mensaje correspondiente
        print("Error: División por cero.")
    #excepción para 'a' cuando se lo intenta convertir a entero
    except ValueError:
        print("Error: Valor no convertible a entero.")
    #por si tuviera una lista o un none, son tipos de datos no compatibles, python espera un número
    except TypeError:
        print("Error: Tipo de dato no compatible.")

#Desafío 69: 
#Escribe una función que calcule el factorial de un número entero positivo. 
# Maneja las excepciones si el número ingresado es negativo, no es entero, 
# o es demasiado grande para ser procesado.

#math para el factorial
import math

#función para calcular el factorial
def factorial(num):
    try:
        #se verifica que el número sea un integer (floats va a levantar error)
        if not isinstance(num, int):
            #si no se ingresa un entero, levanta el error de tipo de dato
            raise TypeError
        #se verifica que el número sea positivo
        if num < 0:
            #si es negativo, se levanta manualmente el error del valor
            raise ValueError
        #si pasa los filtros anteriores se aplica el factorial con math, pasandole ell número como parámetro
        return math.factorial(num)
    #aca se definen los mensajes que van a mostrar los errores
    except ValueError:
        print("Error: El número no puede ser negativo.")
    except TypeError:
        print("Error: El valor debe ser un entero.")
    #este es mas bien anecdótico, porque el limite de un integer en python no es fijo,
    #  está limitado por la memoria del sistema
    except OverflowError:
        print("Error: El número es demasiado grande.")

#se pide por pantalla un número
num = input("Ingrese un número entero positivo: ")
try:
    #se convierte el input (string) a int
    num = int(num)
    #se llama la función y se le pasa el parámetro del input
    resultado = factorial(num)
    #si el resultado es posible (que debería)
    if resultado is not None:
        #se muestra el resultado
        print(f"Factorial: {resultado}")
#por si pasase algo no contemplado
except Exception as e:
    print(f"Error inesperado: {e}")

#Desafío 70: 
#Crea una excepción personalizada llamada NegativeNumberError que se dispare si el 
# usuario intenta ingresar un número negativo en un programa de cálculo de raíces cuadradas. 
# Implementa el manejo de esta excepción en el programa.

#para los calculos
import math

#aca se crea una clase que hereda de exception, no tiene nada porque no se pide
#pero aca se podrían manejar diferentes errores
class NegativeNumberError(Exception):
    pass

#aca se hace una función para calcular la raiz cuadrada
def calcular_raiz(num):
    #aca se verifica si el número ingresado es negativo
    if num < 0:
        #si es negativo se fuerza el error personalizado
        raise NegativeNumberError("No se puede calcular la raíz de un número negativo.")
    #aca se calcula la raiz con math
    return math.sqrt(num)

try:
    #aca se pide un float, si se le pasa un 5, va a leer 5.0
    numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
    #aca se lama la función
    resultado = calcular_raiz(numero)
    #se muestra el resultado por pantalla
    print(f"Raíz cuadrada: {resultado}")
#el error personalizado
except NegativeNumberError as e:
    print("Error:", e)
#por si ingresa algo que no sea un numero
except ValueError:
    print("Error: Entrada no válida.")

#Desafío 71: 
#Desarrolla un programa que abra un archivo de texto, lea su contenido y lo muestre. 
# Implementa manejo de excepciones para archivos que no existan y usa finally 
# para asegurarte de que el archivo se cierre adecuadamente en cualquier caso.

#se define la función, que se le va a pasar el nombre de un archivo
#(esto esta pensado para mi distribución de carpetas)
def leer_archivo(nombre_archivo):
    #se define la ruta usando un f-string
    ruta = f"textos/{nombre_archivo}"
    #se incializa la variable para poder usarla en el finally
    archivo = None
    try:
        #se busca y se trata de abrir el archivo en modo lectura (por eso la "r")
        #y en codificación utf8 que es la estandard
        archivo = open(ruta, "r", encoding="utf-8")
        #si se logró abrir, se usa read para mostar el contenido
        contenido = archivo.read()
        print("Contenido del archivo:")
        #aca se muestra por pantalla
        print(contenido)
    #si no se encontró el archivo
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no existe.")
    #si pasó algo inesperado, se levanta esta exepcion
    except Exception as e:
        #se muesta lo que paso
        print(f"Ocurrió un error al leer el archivo: {e}")
    #una vez que se ejecuto todo, se va al finally
    finally:
        #esto es para cerrar el archivo
        #se verifica si el archivo fue abierto
        if archivo:
            #se cuerra con close
            archivo.close()
            #y un mensaje para mostrar que se cero
            print("Archivo cerrado correctamente.")

#un main para correrlo
if __name__ == "__main__":
    #se pide el nombre del archivo por input
    nombre = input("Ingresa el nombre del archivo (con extension, es decir el formato): ")
    #se le pasa el nombre a la función
    leer_archivo(nombre)