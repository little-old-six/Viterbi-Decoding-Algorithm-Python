import numpy as np
from Tools import O_state
from Tools import H_dis
from Tools import G_out

def CV_Decoding(a, b, m1_num, M1, m):
    c = np.ones(((2 ** m), (m1_num + 1))) * 1000
    c[0, 0] = 0

    J = 1
    while J <= m1_num:
        for i in range(2 ** m):
            K = 1000
            tap = 0
            ham_min = 10000
            for k in range(2 ** m):
                if b[i, J] == 1:
                    if a[k, J - 1, i, J] == 1:
                        I1, J1, I2, J2 = O_state(k, i)
                        X_0, Y_0, U_0 = G_out(I1, J1, I2, J2)
                        ham = H_dis(X_0, Y_0, M1[2 * J - 2], M1[2 * J - 1])
                        if tap == 0:
                            ham_min, tap, K = ham, 1, k
                            c[i, J] = ham + c[k, J - 1]
                        elif ham < ham_min:
                            a[K, J - 1, i, J], K, ham_min = 0, k, ham
                            c[i, J] = ham + c[k, J - 1]
        J += 1

    I, J = 0, 0
    U_out = np.ones(m1_num) * 2
    while (J < m1_num):
        ham_min = 100000000
        U_opt = 2
        I_min = tap = 0
        for i in range(2 ** m):
            if b[i, (J + 1)] == 1:
                if a[I, J, i, J + 1] == 1:
                    I1, J1, I2, J2 = O_state(I, i)
                    X_0, Y_0, U_0 = G_out(I1, J1, I2, J2)
                    ham = c[i, J + 1]
                    if ham <= ham_min:
                        ham_min, U_opt, I_min = c[i, (J + 1)], U_0, i
        U_out[J] = U_opt
        J += 1
        I = I_min
    return U_out


def V_Decoding(a, b, m1_num, M1, m):
    I, J = 0, 0
    U_out = np.zeros(m1_num)
    while (J < m1_num):
        ham_min = 100000000
        U_min = 2
        I_min = 0

        for i in range(2**m):
            if b[i, (J+1)] == 1:
                if a[I, J, i, J+1] == 1:
                    I1, J1, I2, J2 = O_state(I, i)
                    X_0, Y_0, U_0 = G_out(I1, J1, I2, J2)
                    ham = H_dis(X_0, Y_0, M1[2*J], M1[2*J+1])
                    if ham <= ham_min:
                        ham_min = ham
                        U_min = U_0
                        I_min = i
        U_out[J] = U_min
        J += 1
        I = I_min
    return U_out