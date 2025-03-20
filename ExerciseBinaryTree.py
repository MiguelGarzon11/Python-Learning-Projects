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

    
tree = BST()

for value in [20, 10, 30, 5, 15, 25, 35]:
    tree.insert(value)

print("Recorrido en orden:", tree._inorder_traversal())
print("El número más pequeño del árbol es:", tree.find_min())
