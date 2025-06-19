#reinventando_la_rueda.py

def suma(lista):
    #caso base, lista vacia
    if not lista:
        #para que la función termine
        return 0
    else:
        #lista 0 es el primer elemento
        #esta parte va sumando el primer elemento de la lista con el resto de los elementos
        #pero, al llamar suma (la función) lista (el parámetro) y [1:] los intervalos
        #se le está diciendo que una vez que cree una nueva lista sin el primer elemento (el previo)
        #entonces, li la lista es [1,2,3] en la primera "vuelta" va a sumar 1 + [2,3], ahora la lista es [2,3]
        #en la siguente vuelta va a ser 3 (1+2) + [3]
        #luego va a ser 6 + 0 (porque la lista va a quedar vacia y va a ir al caso base y termina la función)
        return lista[0] + suma(lista[1:])

def contar(lista):
        #caso base, lista vacia
    if not lista:
        #para que la función termine
        return 0
    else:
        #similar que arriba, pero para contar todos los elementos de la lista
        #aca se va sumando cada elemento hasta vaciar la lista y obtenerlos todos
        #el 1 sería el primer elemento
        return 1 + contar(lista[1:])

def promedio(lista):
        #para no dividir por 0 si se pasa una lista vacia
        if not lista:
            #error explicando que pasó
            raise ValueError("Lista vacía")
        else:
             return suma(lista)/contar(lista)

def titulo(texto, indice = 0):
    #caso base
    #si la cantidad de letras es mayor a si misma termina la función
    if indice >= contar(texto):
        #retorna un string vacio
        return ""
    #se guarda el caracter actual del texto para poder modificarlo mas abajo
    car_actual = texto[indice]

    #si el índice (osea la posición actual) es la primer letra de la primer palabra
    #o si hay un espacio atras de la letra (comienza una nueva palabra)
    #esta función no contempla el uso de signos como ¿? o !¡
    if indice == 0 or texto[indice - 1] == " ":
        #se convierte el caracter a mayuscula
        car_actual = car_actual.upper()
    #si no, se pasa a minuscula
    else:
        car_actual = car_actual.lower()

    #para que la función siga hasta llegar al caso base
    #por eso se le suma 1 al indice, para que siga avanzando
    return car_actual + titulo(texto, indice + 1)


def mcd(numero_1, numero_2):
    #caso base para terminar la función
    #si el numero 2 es 0, significa que el resto de la operación anterior es 0
    #entonces numero_1 es el número que divide a numero_2 (el anterior) y si mismo
    if numero_2 == 0:
        #se retorna el ultimo número que es el que en la vuelta anterior era numero_2
        return numero_1
    else:
        #segun euclides: El MCD de dos números a y b es el mismo que el MCD de b y el resto de a dividido por b.
        #ni idea la verdad, le pedi ayuda a chatgpt con esta en concreto porque esto me resulta complicado
        #pero en referencia al código, numero_2 esta aca para llegar al caso base
        #numero_1 % numero_2 se fija el resto de la división para saber si es 0
        return mcd(numero_2, numero_1 % numero_2)

#como aparentemente 0 y 1 no son primos, para el caso base use 2 en vez de 0
def es_primo(numero, divisor = 2):
    #para manejar el 0 y el 1
    if numero < 2:
        return False
    #el codigo es simple, pero ni idea del porque pasa, entiendo el código, mas no el concepto matemático
    if divisor * divisor > numero:
        #aparentemente si el resultado de la multiplicacion de dos divisores es mayor que el número
        #ese número es primo
        return True
    #al parecer no pueden haber números divisores, entonces si algún número es divisible no es primo
    if numero % divisor == 0:
        return False
    #aca avanza la función
    #supongo que divisor + 1 es para contemplar todos los números desde el 2 hasta el infinito y mas allá
    return es_primo(numero, divisor + 1)