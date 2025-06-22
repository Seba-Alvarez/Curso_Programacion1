# procesador_texto.py
import string
import os

def leer_texto(nombre_texto):
    #getcwd es un método de os que retorna la dirección de este archivo en el sistema
    #aca se esta guardando la ruta del procesador de texto en una variable
    ruta_base = os.getcwd()
    #aca es la parte importante, no importa donde este el procesador
    #lo importante es que exista una carpeta llamada textos a su mismo nivel
    #y que dentro de la carpeta textos esten los txt que se quieren analizar
    #ruta_base es donde esta el procesador, textos es el nombre de la carpeta
    #nombre_texto es el nombre del texto, esta dentro de un f-string para que pueda leer cualquier txt dentro de la carpeta
    ruta_texto = os.path.join(ruta_base, "textos", f"{nombre_texto}.txt")

    #manejo de excepciones por si no hay ningun texto en la carpeta
    if not os.path.exists(ruta_texto):
        #se muestra el error y donde se esta intentando buscar el texto
        raise FileNotFoundError(f"Archivo no encontrado en {ruta_texto}")
    
    #open es una funcion que abre el archivo para leerlo
    #esta with es para decirle a python que use la funcion y que abra el archivo
    #el primer argumento es la ruta donde esta el texto
    # "r" significa que se abre el texto en modo read (solo lectura)
    #utf-8 es la codificación actual con la que se leen los archivos de texto
    #archivo es el nombre de la variable para trabajar sobre el archivo abierto
    with open(ruta_texto, "r", encoding="utf-8") as archivo:
        #read() "lee" el archivo y lo devuelve como un string para poder aplicar las funciones del procesador
        return archivo.read()

def contar_palabras(texto):
    return len(texto.split())

def verificar_ortografia(texto):
    # Simulamos una función que verifica la ortografía.
    # En una aplicación real, esto podría ser más complejo.
    return "Ortografía verificada."

def ajustar_margenes(texto, margen_izquierdo=10, margen_derecho=10):
    return ' ' * margen_izquierdo + texto + ' ' * margen_derecho


def numeros_mas_legibles(numeros):
    #f-strings te permiten formatear cadenas de texto
    #en este caso, se está usando para que cada 3 números (decena, centena y mil) ponga una coma
    #esto se hace para facilitar la lectura
    #python ya tiene la lógica interna integrada para separar de a mil
    #enonces al poner el argumento :, los : le dicen a python que lo que va despues va a ser el formato
    return f"{numeros:,}"


def formato_titulo(texto):
    #técnicamente una de las pocas funciones globales del módulo
    #esto pone la primera letra de cada palabra en mayuscula
    return string.capwords(texto)

def ascii_validos(texto):
    #se recorre cada caracter en un texto y se verifica con in si está dentro de la lista 
    #   de caracteres ascii en string.printable
    #all va a devolver True(si todos los caracteres son validos) o False( con caracteres no validos como emojis por ejemplo)
    return all(caracter in string.printable for caracter in texto)