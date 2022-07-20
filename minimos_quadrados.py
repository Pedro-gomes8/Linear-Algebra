import numpy as np


def minimos(*args):
    '''Define a funcao y = b1 + b*x que minimiza o erro entre a reta de regressao
    e os pontos experimentais'''
    X = []
    Y = []
    for arg in args:
        X.append(arg[0])
        Y.append(arg[1])
    numero_elementos = len(X)
    A = np.array([[0, 0], [0, 0]], float)
    C = np.array([[0], [0]], float)
    A[0, 0] = numero_elementos
    A[1, 0] = sum(x for x in X)
    A[0, 1] = A[1, 0]
    A[1, 1] = sum(x**2 for x in X)
    C[0] = sum(y for y in Y)
    C[1] = sum(X[i]*Y[i] for i in range(numero_elementos))
    B = np.linalg.solve(A, C)
    print(f'f(x) = {B[0]} + {B[1]}x')
    return B


minimos([1, 2], [2, 3.5], [3, 6.5])
