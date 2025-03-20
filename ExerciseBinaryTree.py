# Primer ejercicio de BinaryTree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
    
    def _inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)

    def find_min(self):
        result = self._inorder_traversal()
        if result:
            minor = result[0]
            for nodo in result[1:]:
                if nodo < minor:
                    minor = nodo
            return minor
    
    def find_max(self):
        result = self._inorder_traversal()
        if result:
            maxi = result[-1]
            for nodo in result:
                if nodo > maxi:
                    maxi = nodo
            return maxi
        
    def delete(self, value):
        if self.root is None:
            return f"ERROR: No hay datos que eliminar"
        else:
            self.root = self._delete_recursive(self.root, value)
            return f"El valor {value} fue eliminado"

    def _delete_recursive(self, current, value):
        if current is None:
            return None
        
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None
            
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            
            successor = self._find_min(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _find_min(self, current):
        while current.left:
            current = current.left
        return current


tree = BST()

for value in [20, 10, 30, 5, 15, 25, 35]:
    tree.insert(value)

print("Recorrido en orden:", tree._inorder_traversal())
print("El número más pequeño del árbol es:", tree.find_min())
print("El número más grande es:", tree.find_max())
print("Se va a eliminar el número 10:", tree.delete(10))
print("Lista actualizada", tree._inorder_traversal())