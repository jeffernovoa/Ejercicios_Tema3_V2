import numpy as np

def determinante_recursivo(matriz):
    """Calcula el determinante de una matriz 3x3 de forma manual."""
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return (a * (e * i - f * h)
            - b * (d * i - f * g)
            + c * (d * h - e * g))

def resolver_cifra_magica():
    """Genera una matriz 3x3 aleatoria y calcula su determinante."""
    matriz = np.random.randint(1, 10, (3, 3))
    print("Matriz:\n", matriz)
    print("Determinante (recursivo):", determinante_recursivo(matriz))
    print("Determinante (iterativo):", round(np.linalg.det(matriz), 2))