class nodo_arbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.altura = 1

def altura(nodo):
    return nodo.altura if nodo is not None else 0

def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def obtener_balance(nodo):
    return altura(nodo.izquierda) - altura(nodo.derecha) if nodo is not None else 0

def rotar_izquierda(z):
    y = z.derecha
    sub_izq = y.izquierda
    y.izquierda = z
    z.derecha = sub_izq
    actualizar_altura(z)
    actualizar_altura(y)
    return y

def rotar_derecha(z):
    y = z.izquierda
    sub_der = y.derecha
    y.derecha = z
    z.izquierda = sub_der
    actualizar_altura(z)
    actualizar_altura(y)
    return y

def insertar(nodo, dato):
    if nodo is None:
        return nodo_arbol(dato)
    if dato < nodo.dato:
        nodo.izquierda = insertar(nodo.izquierda, dato)
    else:
        nodo.derecha = insertar(nodo.derecha, dato)
    actualizar_altura(nodo)
    factor_balance = obtener_balance(nodo)
    if factor_balance > 1 and dato < nodo.izquierda.dato:
        return rotar_derecha(nodo)
    if factor_balance > 1 and dato > nodo.izquierda.dato:
        nodo.izquierda = rotar_izquierda(nodo.izquierda)
        return rotar_derecha(nodo)
    if factor_balance < -1 and dato > nodo.derecha.dato:
        return rotar_izquierda(nodo)
    if factor_balance < -1 and dato < nodo.derecha.dato:
        nodo.derecha = rotar_derecha(nodo.derecha)
        return rotar_izquierda(nodo)
    return nodo

def recorrido_en_orden(nodo):
    if nodo is None:
        return
    recorrido_en_orden(nodo.izquierda)
    print(nodo.dato, end=" ")
    recorrido_en_orden(nodo.derecha)

def imprimir_balances(nodo):
    if nodo is None:
        return
    print(f"{nodo.dato}({obtener_balance(nodo)})", end=" ")
    imprimir_balances(nodo.izquierda)
    imprimir_balances(nodo.derecha)

def validar_avl(nodo):
    if nodo is None:
        return True
    b = obtener_balance(nodo)
    if b < -1 or b > 1:
        return False
    return validar_avl(nodo.izquierda) and validar_avl(nodo.derecha)

def validar_alturas(nodo):
    if nodo is None:
        return True
    esperada = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))
    if nodo.altura != esperada:
        return False
    return validar_alturas(nodo.izquierda) and validar_alturas(nodo.derecha)

def nodo_minimo(nodo):
    cur = nodo
    while cur.izquierda is not None:
        cur = cur.izquierda
    return cur

def borrar(nodo, dato):
    if nodo is None:
        return None
    if dato < nodo.dato:
        nodo.izquierda = borrar(nodo.izquierda, dato)
    elif dato > nodo.dato:
        nodo.derecha = borrar(nodo.derecha, dato)
    else:
        if nodo.izquierda is None or nodo.derecha is None:
            nodo = nodo.izquierda if nodo.izquierda is not None else nodo.derecha
        else:
            temp = nodo_minimo(nodo.derecha)
            nodo.dato = temp.dato
            nodo.derecha = borrar(nodo.derecha, temp.dato)
    if nodo is None:
        return None
    actualizar_altura(nodo)
    factor_balance = obtener_balance(nodo)
    if factor_balance > 1 and obtener_balance(nodo.izquierda) >= 0:
        return rotar_derecha(nodo)
    if factor_balance > 1 and obtener_balance(nodo.izquierda) < 0:
        nodo.izquierda = rotar_izquierda(nodo.izquierda)
        return rotar_derecha(nodo)
    if factor_balance < -1 and obtener_balance(nodo.derecha) <= 0:
        return rotar_izquierda(nodo)
    if factor_balance < -1 and obtener_balance(nodo.derecha) > 0:
        nodo.derecha = rotar_derecha(nodo.derecha)
        return rotar_izquierda(nodo)
    return nodo

def hacer_arbol(valores):
    raiz = None
    for v in valores:
        raiz = insertar(raiz, v)
    return raiz

valores = [13, 7, 15, 3, 8, 14, 14, 14, 10, 27, 17, 8, 52]
raiz = hacer_arbol(valores)

print("recorrido numeros:")
recorrido_en_orden(raiz)
print()
print("balances por nodo:")
imprimir_balances(raiz)
print()
print("AVL:", "sí" if validar_avl(raiz) and validar_alturas(raiz) else "no")

entrada = input("Ingresa el número a borrar: ").strip()
try:
    a_borrar = int(entrada)
    raiz = borrar(raiz, a_borrar)
    print("recorrido despues de borrar:")
    recorrido_en_orden(raiz)
    print()
    print("balances por nodo:")
    imprimir_balances(raiz)
    print()
    print("AVL:", "sí" if validar_avl(raiz) and validar_alturas(raiz) else "no")
except ValueError:
    print("Entrada no válida; no se borró ningún nodo.")
#tare: agregar la rotacion del arbol según el balance de cada nodo hasta que quede balanceado#
