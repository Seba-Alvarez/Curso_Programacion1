#funciones con operaciones: suma, resta, multiplicacion y division
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

#se crea la clase para hacer los nodos
class Nodo:
    #constructor con el valor
    def __init__(self, valor):
        #atributo con el valor para asignarlo en cada nodo
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#funcion para leer las expresiones, y usar las funciones con los operadores
def buscar_operador(expresion, operador):
    #contador inicializado en 0 para manejar las posiciones de los
    #parentesis
    parentesis = 0
    #se recorre la expresion de derecha a izquierda
    #len devuelve el numero de caracteres del string
    for i in range(len(expresion) - 1, -1, -1):
        #si la expresion tiene un parentesis, se le agrega un 1 al contador 
        if expresion[i] == ')':
            parentesis += 1
        #lo mismo que arriba pero se resta 1
        elif expresion[i] == '(':
            parentesis -= 1
        #si no hay parentesis o estan nivelados se retorna el string
        elif expresion[i] == operador and parentesis == 0:
            return i
    #por si no se encuentra operadores fuera de parentesis, se devuelve -1
    return -1

#funcion para armar el arbol en base a la expresion
def construir_arbol_expresion(expresion):
    #aca se remplazan los espacios del string para leer toda la operación junta
    #y que no se tomen los caracteres vacios en cuenta
    expresion = expresion.replace(" ", "")

    #op es operador
    #se maneja primero la suma y la resta, porque tienen menor prioridad
    #a la hora de hacer las operaciones
    for op in ['+', '-']:
        #se usa la funcion de buscar operadores para ver si estan bien puestos
        pos = buscar_operador(expresion, op)
        #si la función no retorno -1
        #ademas funciona como caso base
        if pos != -1:
            #se asigna el valor del nodo
            nodo = Nodo(op)
            #llamada recursiva a la funcion con slicing, a la derecha del : lo esta moviendo a la izquierda
            nodo.izquierda = construir_arbol_expresion(expresion[:pos])
            #llamada recursiva a la funcion con slicing, a la izquierda del : en realidad sería donde para
            #por eso se le suma+1 a la posicion, lo cual lo mueve a la derecha
            nodo.derecha = construir_arbol_expresion(expresion[pos+1:])
            #retorna el valor del nodo
            return nodo

    #se manejan juntas porque tienen mas prioridad que la suma y la resta
    for op in ['*', '/']:
        #lo mismo que arriba, se pasa la posicion para ver si estan bien puestos
        #los parentesis en la operacion
        pos = buscar_operador(expresion, op)
        #igual que arriba
        if pos != -1:
            #igual que arriba
            nodo = Nodo(op)
            #igual que arriba
            nodo.izquierda = construir_arbol_expresion(expresion[:pos])
            #igual que arriba
            nodo.derecha = construir_arbol_expresion(expresion[pos+1:])
            #igual que arriba
            return nodo
    #retorna la expresion completa, ademas transforma el string en un int para hacer la operacion
    return Nodo(int(expresion))

def evaluar_arbol(nodo):
    #caso base 
    if nodo is None:
        return 0
    # Si el valor del nodo es un entero, lo devuelve directamente 
    if isinstance(nodo.valor, int):
        return nodo.valor

    #Evalúa el subarbol izquierdo
    izquierda = evaluar_arbol(nodo.izquierda)
    #Evalúa el subarbol izquierdo
    derecha = evaluar_arbol(nodo.derecha)

    #se hacen las cuentas cuando estan los presentes
    #los caracteres correspondientes
    if nodo.valor == '+':
        return sumar(izquierda, derecha)
    elif nodo.valor == '-':
        return restar(izquierda, derecha)
    elif nodo.valor == '*':
        return multiplicar(izquierda, derecha)
    elif nodo.valor == '/':
        return dividir(izquierda, derecha)

#se guarda la expresion en una variable, aca
#se podria pedir por consola si se quisiera
expresion = "5 + 3 * 4"
#se le pasa la expresion para construir el arbol
arbol = construir_arbol_expresion(expresion)
#se le pasa el arbol ya construido a la funcion para hacer las cuentas
resultado = evaluar_arbol(arbol)

#se muestra la cuenta por pantalla
print(f"El resultado de la expresión '{expresion}' es: {resultado}")