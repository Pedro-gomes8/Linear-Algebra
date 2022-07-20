import numpy as np
from math import sqrt


def jacobi(a, b, iteration_limit=100, tolerancia=1.0e-4):
    size = len(b)
    a = np.array(a, float)
    b = np.array(b, float)
    x = np.array([[1], [1], [1]], float)
    xnew = np.array([[0]]*size, float)

    # for i in range(size):
    #     soma_linha = 0
    #     for j in range(size):
    #         if j != i:
    #             soma_linha += abs(a[i, j])
    #     print(soma_linha)
    #     if (abs(a[i, i]) < soma_linha):
    #         print(
    #             'Condicao de convergencia nao obedecida. A matriz deve ser diagonal dominante!')
    #         return

    for i in range(size):
        if (abs(a[i, i]) < sum(abs(a[i, j]) for j in range(size) if j != i)) or (abs(a[i, i]) < sum(abs(a[j, i]) for j in range(size) if j != i)):
            print(
                "condicao de convergencia nao obedecida. A matriz deve ser diagonal dominante!")
            return -1

    for iteration in range(iteration_limit):
        print(f'iteration: {iteration+1} \n X atual = {x}')
        convergencia = True
        for i in range(size):
            somaj = 0
            for j in range(size):
                if j != i:
                    somaj += a[i, j]*x[j]
            # somaj = sum(a[i, j]*x[j] for j in range(size) if j != i)
            xnew[i] = (b[i] - somaj)/a[i, i]

        # R = sqrt(sum((xnew[i]-x[i])**2 for i in range(size))
        #          )/sqrt(sum(xnew[i]**2 for i in range(size)))

        R = sqrt(sum((xnew[i] - x[i])**2 for i in range(size))
                 )/sqrt(sum(xnew[i]**2 for i in range(size)))

        if R > tolerancia:
            convergencia = False

        if convergencia:
            print('CONVERGEEE!')
            print(xnew)
            return xnew

        x = np.copy(xnew)


H = [[4, 1, 2, -1], [3, 6, -1, 2], [2, -1, 5, -3], [4, 1, -3, -8]]
Y = [[2], [-1], [3], [2]]

# H = [[1, 2, 2], [4, 4, 2], [4, 6, 4]]
# Y = [3, 6, 10]
x = jacobi(H, Y)
