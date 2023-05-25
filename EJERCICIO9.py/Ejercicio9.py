from tda_cola import Cola, cola_vacia, arribo, atencion
from tda_heap import Heap, arribo as arribo_h, heap_vacio, atencion as atencion_h
from tda_heap import cambiar_prioridad, buscar as buscar_h
from tda_lista2 import Lista, barrido, eliminar, insertar
from tda_pila_dinamico import Pila, apilar, pila_vacia, desapilar
from math import inf


class nodoArista(object):
    """Clase nodo vértice."""

    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info, datos=None):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.datos = datos
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista() # lista de aristas


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de arsitas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato, datos=None):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato, datos)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregrar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregrar_arista(destino.adyacentes, dato, origen.info)

def agregrar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                quitar_arista(aux.adyacentes, clave)
            aux = aux.sig
        # aca terminar eliminar aristas adyacenes grafo no dirigido
    return x


def quitar_arista(vertice, destino):
    x = None
    if(vertice.adyacentes.inicio.destino == destino):
        x = vertice.adyacentes.inicio.info
        vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
        vertice.adyacentes.tamanio -= 1
    else:
        ant = vertice.adyacentes.inicio
        act = vertice.adyacentes.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.adyacentes.tamanio -= 1
    return x

def eliminar_arista(grafo, vertice, destino):
    """Elimina una arsita del vertice y lo devuelve si lo encuentra."""
    x = quitar_arista(vertice, destino)    
    
    if(not grafo.dirigido):
        ori = buscar_vertice(grafo, destino)
        quitar_arista(ori, vertice.info)

    return x

def barrido_vertices(grafo):
    """Realiza un barrido de la grafo mostrando sus valores."""
    aux = grafo.inicio
    while(aux is not None):
        print('vertice:', aux.info)
        print('adyacentes:')
        adyacentes(aux)
        aux = aux.sig


def buscar_vertice(grafo, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def tamanio(grafo):
    """Devuelve el numero de vertices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo esta vacio."""
    return grafo.inicio is None

def distancia_maxima(grafo):
    """Devuelve la distancia maxima entre dos vertices del grafo."""
    maximo = 0
    aux = grafo.inicio
    while(aux is not None):
        adyacentes = aux.adyacentes.inicio
        while(adyacentes is not None):
            if(adyacentes.info > maximo):
                maximo = adyacentes.info
            adyacentes = adyacentes.sig
        aux = aux.sig
    return maximo


def adyacentes(vertice):
    """Muestra los adyacents del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig

def marcar_no_visitado(grafo):
    """Marca todos losvertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux.visitado = False
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if(not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_distancia(grafo, distancia):
    """Barrido en profundidad del grafo."""
    aux = grafo.inicio
    while(aux is not None):
        if(aux.adyacentes.inicio is not None):
            adyacentes = aux.adyacentes.inicio
            while(adyacentes is not None):
                if(adyacentes.info == distancia):
                    print(aux.info, str("-"), adyacentes.destino)
                adyacentes = adyacentes.sig
        aux = aux.sig

def barrido_profundidad_distancia(grafo, distancia):
    # dado una distnaica, mostrar todos los vertices que se encuentran a esa distancia
    lista = []
    """Barrido en profundidad del grafo."""
    aux = grafo.inicio
    while(aux is not None):
        if(aux.adyacentes.inicio is not None):
            adyacentes = aux.adyacentes.inicio
            while(adyacentes is not None):
                if(adyacentes.info == distancia) and (aux.info not in lista):
                    lista.append(aux.info)
                adyacentes = adyacentes.sig
        aux = aux.sig
    return barrido_lista(lista)

def barrido_lista(lista):
    for i in range(len(lista)):
        print(lista[i])
