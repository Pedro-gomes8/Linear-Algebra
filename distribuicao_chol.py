import numpy as np
from math import sqrt


def cholesky(a):
    ''' Aplicavel quando a matriz e positiva definida e simetrica'''
    # if not simetrica(a):
    # return "Nao e possivel utilizar cholesky pois a matriz nao e simetrica"
    # if not posdef(a):
    # return "Nao e possivel utilizar cholesky pois a matriz nao e positiva definida"
    size = len(a)
    a = np.array(a, float)
    # Criando uma matriz L de zeros
    L = np.array([[0]*size for i in range(size)], float)

    for j in range(size):
        for i in range(j, size):
            if i == j:  # Se o elemento esta na diagonal principal
                somak = sum(L[i, k]**2 for k in range(j))
                L[i, j] = sqrt(a[i, j] - somak)
            else:
                somak = sum(L[i, k]*L[j, k] for k in range(j))
                L[i, j] = (a[i, j] - somak)/L[j, j]

    # Se temos L, e possivel encontrar U atraves da transposta de L
    U = np.array([[L[j, i] for j in range(size)]
                  for i in range(size)], float)  # Fazendo transposta de L
    return L, U

    # TESTE
H = [[5.2, 3, 0.5, 1, 2],
     [3, 6.3, -2, 4, 0],
     [0.5, -2, 8, -3.1, 3],
     [1, 4, -3.1, 7.6, 2.6],
     [2, 0, 3, 2.6, 15]]


A = [[19, 9, 8, 7, 6, 5, 4, 3, 2, 1],
     [9, 17, 9, 8, 7, 6, 5, 4, 3, 2],
     [8, 9, 18, 9, 8, 7, 6, 5, 4, 3],
     [7, 8, 9, 19, 9, 8, 7, 6, 5, 4],
     [6, 7, 8, 9, 18, 9, 8, 7, 6, 5],
     [5, 6, 7, 8, 9, 17, 9, 8, 7, 6],
     [4, 5, 6, 7, 8, 9, 16, 9, 8, 7],
     [3, 4, 5, 6, 7, 8, 9, 15, 9, 8],
     [2, 3, 4, 5, 6, 7, 8, 9, 14, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]]
b = [[4],
     [0],
     [8],
     [0],
     [12],
     [0],
     [8],
     [0],
     [4],
     [0]]
print(cholesky(A))
