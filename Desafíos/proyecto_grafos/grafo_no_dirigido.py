# grafo_no_dirigido.py

from estructura_lista import ListaAdyacencia

class GrafoNoDirigido:
    def __init__(self, vertices):
        self.V = vertices
        self.lista = [ListaAdyacencia() for _ in range(vertices)]

    def agregar_arista(self, i, j):
        self.lista[i].agregar_nodo(j)
        self.lista[j].agregar_nodo(i)  # Ambos sentidos

    def mostrar_lista(self):
        print("Lista de Adyacencia (Grafo No Dirigido):")
        for i in range(self.V):
            print(f"{i} -> ", end="")
            for destino in self.lista[i].obtener_nodos():
                print(f"{destino} ", end="")
            print()

    def mostrar_edge_list(self):
        print("Edge List (Grafo No Dirigido):")
        mostradas = set()
        for i in range(self.V):
            for destino in self.lista[i].obtener_nodos():
                if (destino, i) not in mostradas:
                    print(f"({i}, {destino})")
                    mostradas.add((i, destino))
