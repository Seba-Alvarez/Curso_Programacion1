# main.py

from grafo_no_dirigido import GrafoNoDirigido
from grafo_dirigido import GrafoDirigido

def main():
    print("=== Grafo No Dirigido ===")
    grafo_nd = GrafoNoDirigido(4)
    grafo_nd.agregar_arista(0, 1)
    grafo_nd.agregar_arista(0, 2)
    grafo_nd.agregar_arista(1, 2)
    grafo_nd.agregar_arista(2, 3)
    grafo_nd.mostrar_edge_list()
    #grafo_nd.mostrar_lista()

    print("\n=== Grafo Dirigido ===")
    grafo_d = GrafoDirigido(4)
    grafo_d.agregar_arista(0, 1)
    grafo_d.agregar_arista(0, 2)
    grafo_d.agregar_arista(1, 2)
    grafo_d.agregar_arista(2, 3)
    grafo_d.mostrar_edge_list()
    #grafo_d.mostrar_lista()

#codigo base afanado de aca:
#https://www.geeksforgeeks.org/dsa/graph-and-its-representations

if __name__ == "__main__":
    main()
