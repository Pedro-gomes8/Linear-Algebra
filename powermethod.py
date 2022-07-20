import numpy as np


def power_method(a, max_iter=100, tolerancia=1.0e-3):
    """Calcula o maior autovalor (em modulo) e seu autovetor correspondente atraves do power method"""
    size = len(a)
    a = np.array(a, float)
    x = np.array(([[1]]*size), float)
    y = np.array(([[0]]*size), float)
    h_anterior = 1  # iniciando-o como 1
    for iteracao in range(max_iter):
        print(
            f'iteracao: {iteracao+1} \n autovalor atual: {h_anterior}')
        toleravel = True
        for i in range(size):
            y[i] = sum(a[i, j]*x[j] for j in range(size))
        h = y[0]
        print(h)
        y = y/h
        print(y)
        R = abs(h - h_anterior)/abs(h)
        print(f'R : {R}')
        if R > tolerancia:
            toleravel = False

        if toleravel:
            return float(h), y

        x = np.copy(y)
        h_anterior = h


a = [[3, 2, 0], [2, 3, -1], [0, -1, 3]]

print(power_method(a))
