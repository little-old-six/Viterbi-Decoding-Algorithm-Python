from Tools import H_compare
from Trellis import C_trellis
from Conv_dec import Conv_recode
from Viterbi_dec import CV_Decoding, V_Decoding

def Viterbi_HIHO(size, m, n):
    a = Conv_recode(size, m, n)
    U_num, M1, U0 = a.Conv_recode()                   # get the received symbols

    a, b = C_trellis(m, U_num)                        # construct viterbi trellis
    # U_mes = V_Decoding(a, b, U_num, M1, m)
    U_mes = CV_Decoding(a, b, U_num, M1, m)           # viterbi decoding（HI-HO
    U_mes = U_mes[: (U_num - m)]                      # Delete redundant code words
    print('HI-HO Viterbi decoding result:', U_mes)

    Pe = H_compare(U0, U_mes) / (len(U0) - m)
    print('Pe =', Pe)
    print('over!')


