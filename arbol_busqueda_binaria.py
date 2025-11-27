class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return TreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def hacer_arbol(values):
    root = None
    for i in values:
        root = insert(root, i)
    return root

values = [13, 7, 15, 3, 8, 14, 19, 18, 10]
root = hacer_arbol(values)

print("recorrido numerods:")
inOrderTraversal(root)
print()
