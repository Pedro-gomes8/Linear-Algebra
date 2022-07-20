import numpy as np
from math import sqrt


def seidel(a, b, iter_limit=100, tolerancia=1.0e-4):
    size = len(b)
    a = np.array(a, float)
    b = np.array(b, float)
    x = np.array([[0]]*size, float)

    for i in range(size):
        if (abs(a[i, i]) < sum(abs(a[i, j]) for j in range(size) if j != i)) or (abs(a[i, i]) < sum(abs(a[j, i]) for j in range(size) if j != i)):
            print(
                "condicao de convergencia nao obedecida. A matriz deve ser diagonal dominante!")
            return -1

    for iteration in range(iter_limit):
        convergencia = True
        tmp = np.copy(x)
        print(f'Iteracao: {iteration}\n X atual: {x}')
        for i in range(size):
            somaj = sum(a[i, j]*x[j]for j in range(size) if j != i)
            x[i] = (b[i] - somaj)/a[i, i]

        R = sqrt(sum((x[i] - tmp[i])**2 for i in range(size))
                 )/sqrt(sum(x[i]**2 for i in range(size)))

        if R > tolerancia:
            convergencia = False

        if convergencia:
            print('CONVERGE')
            return x


H = [[8, 2, -1, 0], [2, -4, 0, 0], [0, -2, 8, -1], [0, 0, -1, 4]]
Y = [[1], [1], [1], [1]]

print(seidel(H, Y))
