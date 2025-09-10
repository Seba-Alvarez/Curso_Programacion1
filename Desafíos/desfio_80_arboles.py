
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def buscar_operador(expresion, operador):
    parentesis = 0
    for i in range(len(expresion) - 1, -1, -1): 
        if expresion[i] == ')':
            parentesis += 1
        elif expresion[i] == '(':
            parentesis -= 1
        elif expresion[i] == operador and parentesis == 0:
            return i
    return -1


def construir_arbol_expresion(expresion):
    expresion = expresion.replace(" ", "")

    for op in ['+', '-']:
        pos = buscar_operador(expresion, op)
        if pos != -1:
            nodo = Nodo(op)
            nodo.izquierda = construir_arbol_expresion(expresion[:pos])
            nodo.derecha = construir_arbol_expresion(expresion[pos+1:])
            return nodo

    for op in ['*', '/']:
        pos = buscar_operador(expresion, op)
        if pos != -1:
            nodo = Nodo(op)
            nodo.izquierda = construir_arbol_expresion(expresion[:pos])
            nodo.derecha = construir_arbol_expresion(expresion[pos+1:])
            return nodo

    return Nodo(int(expresion))

def evaluar_arbol(nodo):
    if nodo is None:
        return 0
    if isinstance(nodo.valor, int):
        return nodo.valor

    izquierda = evaluar_arbol(nodo.izquierda)
    derecha = evaluar_arbol(nodo.derecha)

    if nodo.valor == '+':
        return sumar(izquierda, derecha)
    elif nodo.valor == '-':
        return restar(izquierda, derecha)
    elif nodo.valor == '*':
        return multiplicar(izquierda, derecha)
    elif nodo.valor == '/':
        return dividir(izquierda, derecha)

expresion = "5 + 3 * 4"
arbol = construir_arbol_expresion(expresion)
resultado = evaluar_arbol(arbol)

print(f"El resultado de la expresión '{expresion}' es: {resultado}")

def recorrido_preorden(nodo):
    if nodo:
        print(nodo.valor)
        recorrido_preorden(nodo.izquierda)
        recorrido_preorden(nodo.derecha)