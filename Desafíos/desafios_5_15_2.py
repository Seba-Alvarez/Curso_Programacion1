# Desafío 76: 
#Construye un árbol binario simple con al menos 3 niveles de profundidad. 
# Cada nodo debe contener un número entero como valor. 
# Una vez construido el árbol, implementa una función que imprima los valores de 
# los nodos siguiendo un recorrido en preorden.

#se crea la clase para armar el nodo
class Nodo:
    #se crea el nodo con el constructor
    def __init__(self, valor):
        #el valor se le asigna a cada nodo del arbol
        self.valor = valor
        #se inicializan los nodos de la izquierda como none
        self.izquierda = None
        #aca los de la derecha, esto es para depues llenarlos
        self.derecha = None

#función para recorrer el arbol, se le pasa un nodo como parametro
def recorrido_preorden(nodo):
    #caso base, si existe un nodo
    if nodo:
        #se van tomando sub arboles para hacer el recorrido
        #se imprime el valor del nodo instanciandolo de la calse
        print(nodo.valor)
        #se llama a la función de forma recursiva pero con los nodos
        #de la izquierda y la derecha
        recorrido_preorden(nodo.izquierda)
        recorrido_preorden(nodo.derecha)
        #asi se hace el recorrido preorden, raiz -> izquierda -> derecha

#se define la raiz, el incio del arbol
raiz = Nodo(1)
#se define el hijo izquierdo de la raiz
raiz.izquierda = Nodo(2)
#se define el hijo derecho de la raiz
raiz.derecha = Nodo(3)
#aca se definen los hijos del nodo izquierdo
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
#aca se definen los hijos del nodo derecho
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)
#aca seria la profundidad 3, porque la raiz siempre tiene profundidad 0
raiz.izquierda.izquierda.izquierda = Nodo(8)
#se muestra el arbol pasandole el primer nodo (la raiz) a la funcion
#no se printea porque la función ya lo hace
recorrido_preorden(raiz)


# Desafío 77: 
#Dado un árbol binario con números enteros en cada nodo, implementa una función que recorra 
# el árbol en inorden y calcule la suma de todos los valores almacenados en los nodos. 
# El programa debe devolver el resultado final de la suma.

#funcion recursiva para sumar los nodos en inorden
#se le pasa un nodo como parametro
def suma_inorden(nodo):
    #caso base, si no hay mas nodos
    #tanto para que funcione como para que pare la función
    if nodo is None:
        return 0
    #recursion de la funcion, se usa la función actual dentro de si misma
    #recorre inorden izquierda, nodo actual, derecha
    #arranca por el de mas a la izquierda y va subiendo
    #encuentra el nodo mas a la izquierda por la recursion
    return suma_inorden(nodo.izquierda) + nodo.valor + suma_inorden(nodo.derecha)
    #dicho de otra forma, el recorrido es izquierda->raiz->derecha

#hay que pasarle la raiz para que empiece del principio
resultado = suma_inorden(raiz)
#se muestra por pantalla
print(f"La suma de todos los nodos es: {resultado}")

# Desafío 78: 
#Construye un árbol binario en el que cada nodo contiene un número entero. 
# Implementa una función que recorra el árbol en postorden y devuelva el valor máximo 
# encontrado entre todos los nodos del árbol.

#funcion para encontrar el maximo
def max_postorden(nodo):
    #caso base
    if nodo is None:
        #-inf es un numero negativo bajisimo para comparar
        return float('-inf')
    #se guardan los maximos en variables
    #para comparar los nodos de forma recursiva
    #porque no se le esta pasando max(), sino la esta funcion
    max_izq = max_postorden(nodo.izquierda)
    max_der = max_postorden(nodo.derecha)
    #aca se obtiene el mayor numero de los dos
    #se le pasa el valor del nodo actual y los maximos guardados 
    # en las variables
    return max(nodo.valor, max_izq, max_der)
    #el recorrido postorden es izuierda->derecha->raiz

#se le pasa la raiz a la función
max_valor = max_postorden(raiz)
#se muestra por pantalla
print(f"El valor máximo en el árbol es: {max_valor}")

# Desafío 79: 
#Dado un conjunto de números enteros únicos, construye un árbol de 
# búsqueda binaria (ABB) que inserte los valores de manera que el subárbol 
# izquierdo de cada nodo contenga solo nodos con valores menores, y el subárbol derecho 
# solo nodos con valores mayores. Una vez construido el árbol, implementa una función 
# para buscar un número dado y devuelva si ese número existe en el árbol o no.

#la mayoria del codigo lo saque de aca:
#https://www.w3schools.com/dsa/dsa_data_binarysearchtrees.php
#por eso deje los nombres en ingles, lo que agregue yo esta en español

#Se crea la clase para hacer el nodo
class TreeNode:
    #constructor con el valor del nodo
    def __init__(self, data):
        self.data = data
        #se define los nodos de la izquierda y derecha como none
        self.left = None
        self.right = None

#funcion para insertar los nodos, hay que pasarle un nodo
#y el valor que tiene el nodo andentro
def insert(node, data):
    #caso base para llegar a todos los caminos del arbol y para que
    #salga del bucle cuando no haya mas nodos vacios
    #si el nodo no tiene nada
    if node is None:
        #se devuelve el valor, instanciando la clase TreeNode
        return TreeNode(data)
    #si el valor dentro del nodo es menor al de la clase
    if data < node.data:
        #se guarda el valor en el nodo izquierdo
        node.left = insert(node.left, data)
    #si el valor dentro del nodo es mayor al de la calse
    elif data > node.data:
        #se guarda en el nodo derecho
        node.right = insert(node.right, data)
    #esto es por la forma en la que los valores de los nodos se
    #distribuyen, los valores mas chicos van a la izquierda, mientras
    #que los mas grandes van a la derecha

    return node

#aca se busca el nodo, hay que pasarle un nodo y el valor que se esta buscando
def search(node, target):
    #caso base
    if node is None:
        return False
     #si el valor dentro del nodo es igual al valor buscado, ya lo encontro y sale de
     #la funcion con el return
    if node.data == target:
        return True
    #ademas, si el nodo que se le pasa por parametro es menor que el del nodo de la clase
    #busca por la izquierda del arbol, porque se ubican los valores menores de ese lado
    elif target < node.data:
        return search(node.left, target)
    else:
        #si no es menor, busca por la derecha
        return search(node.right, target)

#aca se recorre el arbol
def inOrderTraversal(node):
    #caso base
    if node is None:
        return
    #recorrido inorder recursivo
    #es decir, busca en este orden por subarboles izquierda->raiz->derecha
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

#lista con los numeros
numeros = [13, 7, 15, 3, 8, 14, 19, 18]  
#raiz vacia para arrancar con la función, esto es porque tiene que empezar por ahi
root = None
for num in numeros:
    #no hay que armar el arbol a mano porque se estan insertando todos los valores
    #dentro de este for
    root = insert(root, num)

#se muestra el recorrido del arbol
print("Recorrido inorder:")
#se llama a la función (que ya tiene return)
inOrderTraversal(root)
print("\n")

#el "target", o, el numero que se quiere encontrar
numero_buscado = 14
#pequeño manejo de excepciones
#para notificar al usuario si se encontro el nodo
#se le pasa la raiz para que arranque desde el incio
if search(root, numero_buscado):
    print(f"El número {numero_buscado} SÍ existe en el árbol.")
else:
    print(f"El número {numero_buscado} NO existe en el árbol.")


# Desafío 80:
# Construir y evaluar un árbol de expresiones para una expresión matemática dada.
#Tu tarea es escribir un programa en Python que haga lo siguiente:

#Construir el Árbol de Expresiones: Dada una expresión matemática en forma de cadena, 
# construir el árbol de expresiones correspondiente. Puedes asumir que la expresión está 
# bien formada y solo contiene números enteros, y los operadores +, -, *, /.

#Evaluar el Árbol de Expresiones: Una vez construido el árbol, 
# evaluarlo y devolver el resultado de la expresión.

#Prueba tu Programa: Utiliza la expresión "5 + 3 * 4" para probar tu programa. 
# El resultado debería ser 17.