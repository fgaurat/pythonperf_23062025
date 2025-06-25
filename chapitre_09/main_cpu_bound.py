import threading
import multiprocessing
import time

def count():
    x = 0
    for _ in range(50_000_000):
        x+=1

def run_seq():
    start = time.perf_counter()
    count()
    count()
    end = time.perf_counter()
    print(f"{end-start:.3}s")

def run_thread():
    start = time.perf_counter()
    th1 = threading.Thread(target=count)
    th2 = threading.Thread(target=count)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    end = time.perf_counter()
    print(f"{end-start:.3}s")

def run_process():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"{end-start:.3}s")


def main():
    # 2.84s
    # run_seq()
    
    # 2.71s
    # run_thread()

    # 1.46s
    run_process()



if __name__ == '__main__':
    main()