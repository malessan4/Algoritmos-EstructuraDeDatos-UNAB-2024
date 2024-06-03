class Nodo:
    def __init__(self, dato, siguiente=None): #None para indicar que es el ultimo
        self.dato = dato
        self.next = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None # en la bibliografia es el header, es el elemento que esta primero en la lista.
        self.len = 0 # longitud de la lista
        
    def insertarAlInicio(self, nodo):
        # si el primer elemento es None lo inserta primero
        if self.primero is None:
            self.primero = nodo
        else:
        # si no es el primero, lo inserta antes
            nuevo_nodo = self.primero # podemos ponerle de  nombre nodo temporal
            self.primero = nodo
            self.primero.next = nuevo_nodo
            
        self.len += 1
    
    

    def insertarAlFinal(self, nodo):
    # si el primer elemento es None lo inserta primero
        if self.primero is None:
            self.primero = nodo
        else:
            nodo_temporal = self.primero
            while(nodo_temporal.next is not None):
                nodo_temporal = nodo_temporal.next
            nodo_temporal.next = nodo
        self.len += 1
    
    
    
    # Devuelve la posicion del elemento que se indica.    
    def posicionElemento(self, valor):
        if self.primero is None:
            raise Exception("Lista Vacia")
        else:
            posicion = 0
            if self.primero.dato == valor:
                return posicion
            else:
                nodo_temporal = self.primero
                while(nodo_temporal.next is not None):
                    nodo_temporal = nodo_temporal.next
                    posicion += 1
                    if nodo_temporal.dato == valor:
                        return posicion
            raise Exception("Valor no encontrado")
    
    # Devuelve y remueve el primer elemento
    def remuevePrimerElemento(self):
        if self.primero is None:
            raise Exception("La lista esta vacia")
        else:
            nodo_temporal = self.primero
            self.primero = self.primero.next
            self.len -= 1
            print(f"Elemento removido: {nodo_temporal.dato}")
            return nodo_temporal
        
    def remueveUltimoElemento(self):
        if self.primero is None:
            raise Exception("La lista esta vacia")
        else:
            
        
    def remueveElemento(self, valor):
        pass
    
    def remueveIndice(self, indice):
        pass
    
    def elementoPorIndice(self, indice):
        pass

# si el primer elemento es distino de None, crea una variable que va a ir almacenando las representaciones de la lista        
# y usa una variabe llamada nodo que es la que va ir recorriendo cada uno los nodos creados en la lista   
# se guarda el primero y a la lista le agrego el dato del primer nodo
# despues se pregunta, tengo siguiente? 
# si tiene siguiente me paso al sigiuente nodo, le agrego un espacio, le inserto el dato del nuevo nodo y pregunta nuevamente  
# si no tiene siguiente se cierra la lista con un corchete  


# Representacion en forma de string de la ListaEnlazada                
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
# my_lista.posicionElemento(1) levanta una exception porque la lista esta vacia
# lista en 0

# los uso para separar las cosas en la consola
print(" ")
print(" ")


nodo_x = Nodo(3) # genero un nodo cualquiera
my_lista.insertarAlInicio(nodo_x) # invoco el metodo para insertar y le inserto el nodo_x

nodo_y = Nodo(9)
my_lista.insertarAlInicio(nodo_y)

nodo_z = Nodo(4)
my_lista.insertarAlFinal(nodo_z)

nodo_a = Nodo(2)
my_lista.insertarAlInicio(nodo_a)


print(my_lista)
print(f"La longitud de la lista es: {my_lista.len}")
print(f"Posición del elemento 9: {my_lista.posicionElemento(9)}")
print(" ")

my_lista.remuevePrimerElemento()
print(my_lista)
print(f"La longitud de la lista es: {my_lista.len}")
print(" ")

my_lista.remuevePrimerElemento()
print(my_lista)
print(f"La longitud de la lista es: {my_lista.len}")
print(" ")

my_lista.remuevePrimerElemento()
print(my_lista)
print(f"La longitud de la lista es: {my_lista.len}")
print(" ")