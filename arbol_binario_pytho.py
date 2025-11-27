class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def new_node():
    return Node()


def pre_order(nodo):
    if nodo is None:
        return
    print(nodo.value, end=" ")
    pre_order(nodo.left)
    pre_order(nodo.right)


def in_order(nodo):
    if nodo is None:
        return
    in_order(nodo.left)
    print(nodo.value, end=" ")
    in_order(nodo.right)


def post_order(nodo):
    if nodo is None:
        return
    post_order(nodo.left)
    post_order(nodo.right)
    print(nodo.value, end=" ")


root = new_node()
root.value = "R"
root.left = new_node()
root.left.value = "A"
print(root.left.value)
root.right = new_node()
root.right.value = "B"
root.left.left = new_node()
root.left.left.value = "C"
root.left.right = new_node()
root.left.right.value = "D"
root.right.left = new_node()
root.right.left.value = "E"
root.right.right = new_node()
root.right.right.value = "F"
root.right.right.left = new_node()
root.right.right.left.value = "G"

print("\nPre-order traversal:")
pre_order(root)
print("\nIn-order traversal:")
in_order(root)
print("\nPost-order traversal:")
post_order(root)
