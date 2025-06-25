from multiprocessing import Pool
import os
import time


def f(x):
    t = 1
    start = time.time()
    while time.time()-start<t:
        pass
    return x*x


def main():
    print(os.cpu_count())
    with Pool(2) as p:
        print(p.map(f, range(100)))

if __name__ == '__main__':
    main()