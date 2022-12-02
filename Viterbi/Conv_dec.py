import numpy as np
import random


class Conv_recode:
    def __init__(self, size, m, n):
        self.size, self.m, self.n = size, m, n

    def Conv_recode(self):
        U = np.random.randint(0, 2, self.size)
        M = []
        U = list(U)
        U0 = U.copy()

        print('Origional message symbol：', U)
        U = U + [0] * self.m
        m_num = len(U)

        S = 0
        for i in range(m_num):
            S, X0, X1 = self.C_relationship(S, U[i])
            M = M + [X0] + [X1]

        r = random.sample(range(0, (self.m * self.size)), self.n)
        print('The number of noise is :', self.n, '    The location of noise:', r)
        for i in r:
            M[i] = 1 - M[i]

        if self.n == 0:
            print('Received symbol:', M)
        else:
            print('Received symbol with noise:', M)

        return m_num, M, U0

    def C_relationship(self, S, I):
        if (S == 0) and (I == 0):
            return 0, 0, 0
        elif (S == 0) and (I == 1):
            return 10, 1, 1
        elif (S == 1) and (I == 0):
            return 0, 1, 1
        elif (S == 1) and (I == 1):
            return 10, 0, 0
        elif (S == 10) and (I == 0):
            return 1, 1, 0
        elif (S == 10) and (I == 1):
            return 11, 0, 1
        elif (S == 11) and (I == 0):
            return 1, 0, 1
        elif (S == 11) and (I == 1):
            return 11, 1, 0