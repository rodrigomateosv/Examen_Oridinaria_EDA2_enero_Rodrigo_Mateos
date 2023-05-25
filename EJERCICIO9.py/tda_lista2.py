class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = Lista()


class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or criterio(lista.inicio.info,campo)>criterio(nodo.info,campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo)<criterio(nodo.info,campo)):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    


def eliminar(lista, clave, campo=None):
    dato = None
    if(criterio(lista.inicio.info,campo) == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and criterio(act.info,campo) != clave):
            act = act.sig
            ant = ant.sig
        
        if(act is not None):
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1

    return dato



def busqueda(lista, clave, campo=None):
    aux = lista.inicio
    while(aux is not None and criterio(aux.info, campo) != clave):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def barrido_con_sublista(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        barrido(aux.sublista)

        aux = aux.sig  

def tamanio(lista):
    return lista.tamanio


def lista_vacia(lista):
    return lista.inicio is None


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]



class Alumno(object):

    def __init__(self, apellido, nombre, legajo):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo

    def __str__(self):
        return self.apellido + " " + self.nombre

class Parcial(object):

    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return self.materia + " " + self.nota


class Usuario(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Commit(object):

    def __init__(self, timestamp, msj, archivo, cantidad_lineas):
        self.timestamp = timestamp
        self.msj = msj
        self.archivo = archivo
        self.cantidad_lineas = cantidad_lineas

    def __str__(self):
        return self.msj+' '+ self.archivo+ ' ' + str(self.cantidad_lineas)

lista = Lista()

usuario = Usuario('walter')
insertar(lista, usuario, 'nombre')
usuario = Usuario('tito')
insertar(lista, usuario, 'nombre')
usuario = Usuario('ana')
insertar(lista, usuario, 'nombre')

commit = Commit('11-11-20 19:00', 'cambio en tda hash', 'test1.py', 30)
posicion = busqueda(lista, 'walter', 'nombre')
insertar(posicion.sublista, commit, 'archivo')
commit = Commit('11-11-20 19:00', 'last update tda hash', 'tda_hash.py', -15)
insertar(posicion.sublista, commit, 'archivo')
commit = Commit('11-11-20 19:00', 'update lista de lista', 'test.py', 20)
posicion = busqueda(lista, 'tito', 'nombre')
insertar(posicion.sublista, commit, 'archivo')

# barrido(lista)

mayor = 0
aux = lista.inicio
while(aux is not None):
    if(tamanio(aux.sublista) > mayor):
        mayor = tamanio(aux.sublista)
    aux = aux.sig

aux = lista.inicio
while(aux is not None):
    if(tamanio(aux.sublista) == mayor):
        print(aux.info)
    aux = aux.sig



maximo = 0
usuario = ''
aux = lista.inicio
while(aux is not None):
    sublista = aux.sublista.inicio
    maximo_usuario = 0
    while(sublista is not None):
        maximo_usuario += sublista.info.cantidad_lineas
        sublista = sublista.sig
    if(maximo_usuario > maximo):
        maximo = maximo_usuario
        usuario = aux.info.nombre
    aux = aux.sig

print(usuario, maximo)

aux = lista.inicio
while(aux is not None):
    pos = busqueda(aux.sublista, 'test.py', 'archivo')
    if(pos is not None):
        print(aux.info)
    aux = aux.sig
