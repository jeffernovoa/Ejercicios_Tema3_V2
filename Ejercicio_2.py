import numpy as np

def determinante_recursivo(matriz):
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])
            - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])
            + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

def determinante_iterativo(matriz):
    return np.linalg.det(matriz)

def resolver_cifra_magica():
    matriz = np.random.randint(1, 10, (3, 3))
    print("Matriz:")
    print(matriz)
    if matriz.shape == (3, 3):
        print("Determinante (recursivo):", determinante_recursivo(matriz))
        print("Determinante (iterativo):", determinante_iterativo(matriz))
    else:
        print("Error: La matriz no es de tamaño 3x3.")