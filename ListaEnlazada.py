class Nodo:
    def __init__(self, dato, siguiente=None): #None para indicar que es el ultimo
        self.dato = dato
        self.next = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None # en la bibliografia es el header, es el elemento que esta primero en la lista.
        self.len = 0 # longitud de la lista
        
    def insertarAlInicio(self, nodo):
        if self.primero is None:
            self.primero = nodo
            return
        else:
            nuevo_nodo = self.primero # podemos ponerle de  nombre nodo temporal
            self.primero = nodo
            self.primero.next = nuevo_nodo
            
        self.len += 1
        
    def __str__(self):
        if self.primero is None:
            return "[]"
        else:
            str_lista = "[ "
            nodo = self.primero
            str_lista += str(self.primero.dato)
            while(nodo.next is not None):
                nodo = nodo.next
                str_lista += 1

            
            
                    
my_lista = ListaEnlazada()
print (my_lista.len)


# lista en 0

nodo_x = Nodo(3) # genero un nodo cualquiera
my_lista.insertarAlInicio(nodo_x) # invoco el metodo para insertar y le inserto el nodo_x

nodo_y = Nodo(9)
my_lista.insertarAlInicio(nodo_y)

print (my_lista.len)

