import numpy as np

h = [[3, 3, 0], [6, 5, 8], [0, -1, 3]]


def funcao(x):
    return (4.5 - 6.1*x + 2.5*x**2)


for i in range(1, 5):
    print(funcao(i))
