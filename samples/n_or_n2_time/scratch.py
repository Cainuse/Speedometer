from samples.n_or_n2_time.scratch2 import scratch2

import sys

class test_methods:

    def o_n(n):
        while n > 0:
            n-=1

    def o_n2(n):
        n0 = n
        while n > 0:
            m = n0
            while m > 0:
                m-=1
            n-=1
        print(n)

if __name__ == "__main__":
    if sys.argv[2] == "2":
        test_methods.o_n2(int(sys.argv[1]))
        scratch2.oo_n2(int(sys.argv[1]))
    if sys.argv[2] == "1":
        test_methods.o_n(int(sys.argv[1]))
        scratch2.oo_n(int(sys.argv[1]))


