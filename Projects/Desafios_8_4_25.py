
"""
declarar una variable numerica que sea igual a 0
pedir la cantidad de números que se desea sumar
se hace un bucle para recorrer la cantidad de números deseados
por cada número en el rango especificado
se suma el número actual a la variable
se imprime por pantalla el resultado
"""

"""
#se define la variable como 0, para que no sume ni reste a la hora de hacer la suma de números
variable_1 = 0
#se piden los números
print("ingresar la cantidad de números que se desea sumar")
#se pide por pantalla
variable_2 = int(input())

#se recorren los números desde el 1, hasta el número ingresado + 1
#el +1 es para que el número ingresado sea incluido
for i in range(1, variable_2+1):
    #se suma el número a la variable
    variable_1 += i

#se imprime por consola con un f-string
print(f"La suma de los primeros {variable_2} números naturales es {variable_1}")

"""



"""
se crea una variable para pedir los números
se crea una lista donde se agregan los números
se hace un búcle para agregar la cantidad de números especificados a la lista
se crea una nueva lista, donde se recorren todos los números de la primera lista verificando e ingresando si son pares
se crea una variable para guardar la cantidad de números recorridos
se imprimen por pantalla la cantidad de números pares
    
"""

"""

#se piden los números para la lista
print("ingresar números separados por espacios")
num_ent = input()

#este int es para pasar los strings que recibe a int
#el primer i es el número que se esta recorriendo
#el segundo i es el que se va a ingresar a la lista
#.split es para que el sistema te permita ingresar con espacios
lista_num = [int(i) for i in num_ent.split()]

#se crea una nueva lista, donde se va a filtrar solo los pares
#donde el primer num_de_la_lista es el número que se esta recorriendo de la lista lista_num
#el segundo num_de_la_lista es el mismo número que si es par se va a agregar a la nueva lista num_pares
num_pares = [num_de_la_lista for num_de_la_lista in lista_num
             #si el resto de la división entre 2 es 0, significa que es par y se agrega a la lista
             if num_de_la_lista % 2 == 0]
#la cantidad de números pares es el largo de posiciones de la lista num_pares
cant_num_pares = len(num_pares)

#se imprime la cantidad
print(f"la cantidad de números pares es {cant_num_pares}")


"""

"""
se definen las variables num1, num2 y num3 y se piden los números
se crea la lista con los números
se ordenan los números ingresados
se imprimen por pantalla
"""

"""
#se piden los números
print("ingresar el primer número")
num1 = int(input())
print("ingresar el segundo número")
num2 = int(input())
print("ingresar el tercer número")
num3 = int(input())

#se crea la lista
lista_num = [num1, num2, num3]

#se ordena la lista
lista_num.sort()

#se imprima la lista por consola
print(f" La lista ordenada de forma ascendente: {lista_num}")

"""


"""
se importan la libreria de estadísticas de python
se crea la lista de números
se calcula el promedio de los números
se muestra el resultado
"""

"""

#esto se usa para traer métodos y funciones que tiene python
import statistics

print("ingresar las 5 calificaciones")

#list es para crear la lista
#map es para transformar todos los números ingresados a int (valor numérico)
#.split es para poder ingresar los números separados por espacios
lista_cal= list(map(int, input().split()))

print("las calificaciones ordenadas:")
#.mean significa el promedio o average, en este caso el promedio de los números de la lista
print(statistics.mean(lista_cal))

"""

"""
(las formulas me las robe de chatgpt porque no encaro mucho entendiendo formulas)

se hace una función que haga los calculos para transformar de celsius a fahrenheit (f = (9/5 * c)+32)
se hace una función que haga los calculos para transformar de celsius a kelvin (k = c + 273,15)
se define el número que en celsius que se quiere convertir
se llama a la función de pasar a fahrenheit y se le pasa el número en celsius por parametro
se llama a la función de pasar a kelvin y se le pasa el número en celsius por parametro
se imprime los resultados por pantalla

"""

"""

#dos funciones que hacen los calculos para hacer las conversiones

#para pasar de celsius a fahrenheit la formula es el número en celsius multiplicado por la division de 9/5 y a eso se le suma 32
def cel_far(cel):
    return (9 / 5) * cel + 32

#para pasar de celsius a kelvin la formula es la temperatura en celsius + 273.15
def cel_kel(cel):
    return cel + 273.15

print("ingresar el número a convertir")
#se pide el número que se desea convertir
num_a_conv = float(input())

#se llama a las funciones y se les pasa por parametro el número que se ingrese por consola
far = cel_far(num_a_conv)
kel = cel_kel(num_a_conv)

print(f"{num_a_conv} grados celsius en fahrenheit son {far}")
print(f"{num_a_conv} grados celsius en kelvin son {kel}")

"""

"""
se pide el número que se desea comparar
se guardan los valores en una lista
se recorre la lista
se verifica si el número ingresado es divisible por el número actual que esta recorriendo
se muestra por pantalla si el número es divisible o no
"""

"""

#se pide el número a comparar
print("ingresar el numero que se desea verificar")
num_ing = int(input())

#se guardan los valores que se piden en una lista
es_mul = [2,3,5,7,9,10,11]

#se recorre la lista
#i es el número que está recorriendo
for i in es_mul:
    #si el número ingresado es divisible por el número que esta recorriendo
    if num_ing % i == 0:
        #se imprime que el número es divisible
        print(f"El número: {num_ing} es múltiplo de {i}")
    
    else:
        # si no fuera divisible se imprime que no es
        print(f"{num_ing} no es múltiplo de {i}")

"""

"""
se definen dos variables numéricas
se verifica que la segunda variable no pueda ser 0
si no es 0 se hace la división y se guarda el resto en una variable
se imprime la información por pantalla

"""

"""

print("ingresar el primer número")
num1 = int(input())

print("ingresar el segundo número")
num2 = int(input())

if num2 == 0:
    print("el número a dividir no puede ser 0")
else:
    mod = num1 % num2
    print(f"el resto de:{num1} dividido:{num2} es:{mod}")

"""