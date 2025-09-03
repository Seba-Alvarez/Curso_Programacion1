# estructura_lista.py

class Nodo:
    def __init__(self, destino):
        self.destino = destino
        self.siguiente = None

class ListaAdyacencia:
    def __init__(self):
        self.cabeza = None
        self.cola = None  # Para FIFO

    def agregar_nodo(self, destino):
        nuevo_nodo = Nodo(destino)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def obtener_nodos(self):
        actual = self.cabeza
        while actual:
            yield actual.destino
            actual = actual.siguiente
