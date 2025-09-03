# grafo_dirigido.py

from estructura_lista import ListaAdyacencia

class GrafoDirigido:
    def __init__(self, vertices):
        self.V = vertices
        self.lista = [ListaAdyacencia() for _ in range(vertices)]

    def agregar_arista(self, origen, destino):
        self.lista[origen].agregar_nodo(destino)  # Solo una dirección

    def mostrar_lista(self):
        print("Lista de Adyacencia (Grafo Dirigido):")
        for i in range(self.V):
            print(f"{i} -> ", end="")
            for destino in self.lista[i].obtener_nodos():
                print(f"{destino} ", end="")
            print()

    def mostrar_edge_list(self):
        print("Edge List (Grafo Dirigido):")
        for i in range(self.V):
            for destino in self.lista[i].obtener_nodos():
                print(f"({i} -> {destino})")
