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
        else:
            nuevo_nodo = self.primero # podemos ponerle de  nombre nodo temporal
            self.primero = nodo
            self.primero.next = nuevo_nodo
            
        self.len += 1
        
# si el primer elemento es distino de None, crea una variable que va a ir almacenando las representaciones de la lista        
# y usa una variabe llamada nodo que es la que va ir recorriendo cada uno los nodos creados en la lista   
# se guarda el primero y a la lista le agrego el dato del primer nodo
# despues se pregunta, tengo siguiente? 
# si tiene siguiente me paso al sigiuente nodo, le agrego un espacio, le inserto el dato del nuevo nodo y pregunta nuevamente  
# si no tiene siguiente se cierra la lista con un corchete  
                
    def __str__(self):
        if self.primero is None: 
            return "[]"
        else:
            str_lista = "[ " #abrimos un corchete para la lista
            nodo = self.primero
            str_lista += str(self.primero.dato)
            while(nodo.next is not None):
                nodo = nodo.next # el nodo pasa a ser el siguiente
                str_lista += " " # le agregamos un espasio al string de la lista
                str_lista += str(nodo.dato) # le insertamos al string de la lista del dato del nodo
            str_lista += " ]" # se cierra el corchete de la lista
            return str_lista

            
            
                    
my_lista = ListaEnlazada()
print(my_lista.len)
print(my_lista)


# lista en 0

nodo_x = Nodo(3) # genero un nodo cualquiera
my_lista.insertarAlInicio(nodo_x) # invoco el metodo para insertar y le inserto el nodo_x

nodo_y = Nodo(9)
my_lista.insertarAlInicio(nodo_y)

nodo_z = Nodo(4)
my_lista.insertarAlInicio(nodo_z)

print (my_lista.len)
print(my_lista)
