class nodo_arbol:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
def insert(node, data):
    if node is None:
        return nodo_arbol(data)
    if data < node.data:
        node.left = insert(node.left, data)
    if data > node.data:
        node.right = insert(node.right, data)
    elif data == node.data:
        node.right = insert(node.right, data)
    return node

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def delete(node, data):
    if node is None:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
        return node
    if data > node.data:
        node.right = delete(node.right, data)
        return node
    if node.left is None and node.right is None:
        return None
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left
    nuevo_padre = node.right
    huerfano_menor = node.left
    cur = nuevo_padre
    while cur.left is not None:
        cur = cur.left
    cur.left = huerfano_menor
    return nuevo_padre

def hacer_arbol(values):
    root = None
    for i in values:
        root = insert(root, i)
    return root

values = [13, 7, 15, 3, 8, 14, 14, 14, 10, 27, 17, 8, 52]
root = hacer_arbol(values)

print("recorrido numeros:")
inOrderTraversal(root)
print()

to_delete = int(input("Ingresa el número a borrar: "))
root = delete(root, to_delete)
print("recorrido despues de borrar:")
inOrderTraversal(root)
print()

