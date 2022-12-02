import numpy as np
from Tools import G_in


def C_trellis(m, m1_num):
    a = np.zeros(((2 ** m), (m1_num + 1), (2 ** m), (m1_num + 1)))
    b = np.zeros(((2 ** m), (m1_num + 1)))
    b[0, 0] = 1

    for j in range(m1_num):
        for i in range(2 ** m):
            if j < (m1_num - m):
                if b[i, j] == 1:
                    X = G_in(0, i)
                    a[i, j, X, (j + 1)] = b[X, (j + 1)] = 1

                    X = G_in(1, i)
                    a[i, j, X, (j + 1)] = b[X, (j + 1)] = 1
            else:
                if b[i, j] == 1:
                    X = G_in(0, i)
                    a[i, j, X, (j + 1)] = b[X, (j + 1)] = 1
    return a, b