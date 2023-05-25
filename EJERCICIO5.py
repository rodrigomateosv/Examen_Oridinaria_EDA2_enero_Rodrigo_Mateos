class Nodo:
    def __init__(self, id):
        self.id = id
        self.vecinos = []

class Grafo:
    def __init__(self):
        self.nodos = [Nodo(i) for i in range(10)]
        
    def agregar_conexion(self, origen, destino):
        self.nodos[origen].vecinos.append(self.nodos[destino])

grafo = Grafo()

# Definimos las conexiones basado en tu descripción
grafo.agregar_conexion(1, 6)
grafo.agregar_conexion(1, 8)
grafo.agregar_conexion(2, 7)
grafo.agregar_conexion(2, 9)
grafo.agregar_conexion(3, 4)
grafo.agregar_conexion(3, 8)
grafo.agregar_conexion(4, 3)
grafo.agregar_conexion(4, 9)
grafo.agregar_conexion(4, 0)
grafo.agregar_conexion(6, 1)
grafo.agregar_conexion(6, 7)
grafo.agregar_conexion(6, 0)
grafo.agregar_conexion(7, 2)
grafo.agregar_conexion(7, 6)
grafo.agregar_conexion(8, 1)
grafo.agregar_conexion(8, 3)
grafo.agregar_conexion(9, 2)
grafo.agregar_conexion(9, 4)
grafo.agregar_conexion(0, 4)
grafo.agregar_conexion(0, 6)
