# Ejercicio 1 Binary Search Tree

class Node: # Se crea un nodo
    def __init__(self, value):
        self.value = value  # Guarda el valor del nodo
        self.left = None    # Referencia al hijo menor (izquierda)
        self.right = None   # Referencia al hijo mayor (Derecha)

# Se crea la estructura del árbol

class BST:  # Representa al árbol completo
    def __init__(self):
        self.root = None    # Inicialmente el árbol está vacio.
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value) # Si el árbol esta vacio, creamos la raiz
        else:
            self._insert_recursive(self.root, value)    # Si ya tiene un valor lo ubicamos en la posición correcta con _insert_recursive()

    def _insert_recursive(self, current, value):
        if value < current.value:   # Si el valor es menor, va a la izquierda.
            if current.left is None:
                current.left = Node(value)  # Si el espacio está vacio insertamos el nodo.
            else:
                self._insert_recursive(current.left, value) # Si no, seguimos buscando.
        else:   # Si el valor es mayor o igual, va a la derecha
            if current.right is None:
                current.right = Node(value) # Si el espacio está vacio, insertamos el nodo.
            else:
                self._insert_recursive(current.right, value) # Si no, seguimos buscando.


    def inorder_traversal(self):    # Recorremos el árbol en orden ascendente.
        result = [] # Lista donde guardamos los valores ordenados.
        self._inorder_recursive(self.root, result)   # Llamamos a la función recursiva.
        return result   # Retornamos la lista con los valores ordenados

    def _inorder_recursive(self, current, result):
        if current: # Si el nodo actual no es None:
            self._inorder_recursive(current.left, result)   # Visitamos el hijo izquierdo.
            result.append(current.value)    # Guardamos el valor del nodo actual.
            self._inorder_recursive(current.right, result)  # Visitamos el hijo derecho.

    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current, value):
        if current is None:
            return False # Si llegamos a un nodo vacio, el valor no está en el árbol.
        if current.value == value:
            return True # Si encontramos el valor, retornamos True.
        if value < current.value:
            return self._search_recursive(current.left, value)  # Si el valor es menor Buscamos en la izquierda.
        return self._search_recursive(current.right, value) # Si el valor es mayor Buscamos en la derecha.