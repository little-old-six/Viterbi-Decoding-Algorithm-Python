import numpy as np

def G_out(i1, j1,i2,j2):
    x = i1 * 10 + j1
    y = i2 * 10 + j2

    if (x == 0) and (y == 0):
        return 0, 0, 0
    elif x == 0 and y == 10:
        return 1, 1, 1
    elif x == 1 and y == 0:
        return 1, 1, 0
    elif x == 1 and y == 10:
        return 0, 0, 1
    elif x == 10 and y == 1:
        return 1, 0, 0
    elif x == 10 and y == 11:
        return 0, 1, 1
    elif x == 11 and y == 1:
        return 0, 1, 0
    elif x == 11 and y == 11:
        return 1, 0, 1


def H_dis(i1, j1, i2, j2):
    D = 0
    if i1 != i2:
        D += 1
    if j1 != j2:
        D += 1

    return D


def O_state(I, J):
    X1 = Y1 = X2 = Y2 = 0

    if I == 0:
        X1 = Y1 = 0
    elif I == 1:
        X1, Y1 = 0, 1
    elif I == 2:
        X1, Y1 = 1, 0
    elif I == 3:
        X1 = Y1 = 1

    if J == 0:
        X2 = Y2 = 0
    elif J == 1:
        X2, Y2 = 0, 1
    elif J == 2:
        X2, Y2 = 1, 0
    elif J == 3:
        X2 = Y2 = 1

    return X1, Y1, X2, Y2


def G_in(x, I):
    Y = 5

    if (I == 0) and (x == 0):
        Y = 0
    elif (I == 0) and (x == 1):
        Y = 2

    if (I == 1) and (x == 0):
        Y = 0
    elif (I == 1) and (x == 1):
        Y = 2

    if (I == 2) and (x == 0):
        Y = 1
    elif (I == 2) and (x == 1):
        Y = 3

    if (I == 3) and (x == 0):
        Y = 1
    elif (I == 3) and (x == 1):
        Y = 3

    return Y


def H_compare(M0, M1):
    dis = 0
    l = len(M0)
    for i in range(l):
        if M1[i] != M0[i]:
            dis += 1
    return dis