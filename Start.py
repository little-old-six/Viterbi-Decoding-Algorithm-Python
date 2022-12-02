import sys
sys.path.append(r'..\Viterbi decoding (HI-HO)\Viterbi')

from Viterbi_main import Viterbi_HIHO

if __name__ == '__main__':
    m = 2                    # number of registers in this conv. code
    size = 30                # number of message symbols
    n = 0                    # number of errors

    Viterbi_HIHO(size, m, n)