from numpy import linalg
import numpy as np


def multiplica_matriz(a, b):
    size = len(a)
    c = np.array([[0]*len(a) for i in range(len(a))], float)
    for i in range(size):
        for j in range(size):
            c[i, j] = sum(a[i, k]*b[k, j] for k in range(size))

    return c


def transposta(a):
    size = len(a)
    c = np.array([[0]*len(a) for i in range(len(a))], float)
    for i in range(size):
        for j in range(size):
            c[i, j] = a[j, i]
    return c


def eigen_jacob(a, max_iter=100, tolerancia=1.0e-3):
    size = len(a)
    a = np.array(a, float)
    # Criando matriz identidade inicial X
    x = np.array([[0]*size for i in range(size)], float)
    for i in range(size):
        x[i, i] = 1

    p_inicial = np.copy(x)

    for iteration in range(max_iter):
        p = np.copy(p_inicial)
        maior_valor = 0
        for i in range(size):
            for j in [z for z in range(size) if z != i]:
                if abs(a[i, j]) > abs(maior_valor):
                    linha = i
                    coluna = j
                    maior_valor = a[i, j]

        if abs(maior_valor) <= tolerancia:
            print(f"Numero de iteracoes: {iteration+1}")
            auto_valores = [a[i, i] for i in range(len(a))]
            return auto_valores, x

        if a[linha, linha] == a[coluna, coluna]:
            phi = np.pi/4.0
        else:
            fracao = 2.0*maior_valor/(a[linha, linha]-a[coluna, coluna])
            phi = np.arctan(fracao)/2

        seno_phi = np.sin(phi)
        cos_phi = np.cos(phi)
        p[linha, coluna] = -seno_phi
        p[coluna, linha] = seno_phi
        p[linha, linha] = cos_phi
        p[coluna, coluna] = cos_phi
        # Normalizar y!
        transp = transposta(p)
        x = multiplica_matriz(x, p)
        trans_vezes_a = multiplica_matriz(transp, a)
        a = multiplica_matriz(trans_vezes_a, p)


a = [[3, 2, 0], [2, 3, -1], [0, -1, 3]]
auto_valores, auto_vetores = eigen_jacob(a)
print(f'Auto valores: {auto_valores}\n Auto vetores:\n {auto_vetores}')

z = np.dot([[1/5.23, 0, 0], [0, 1/.76, 0], [0, 0, 1/3]],
           np.transpose(auto_vetores))
y = np.dot(z, [[1], [-1], [1]])
print(y)
print(np.dot(auto_vetores, y))
