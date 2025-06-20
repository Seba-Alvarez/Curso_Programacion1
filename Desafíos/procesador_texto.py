# procesador_texto.py
import string

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