# 多进程编程
# 耗cpu的操作, 用多进程编程, 对于io操作来说,瓶颈不在CPU, 所以用多线程.
# 进程切换代价高于线程,
# 1. 对于耗费CPU的操作,(计算), 多进程优于多线程

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import  ProcessPoolExecutor
import random

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    # 多线程
    # with ThreadPoolExecutor(3) as executor:
#     #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
#     #     start_time = time.time()
#     #     for future in as_completed(all_task):
#     #         data = future.result()
#     #         print("exe {} data".format(data))
#     #
#     #     print("last time is : {}".format(time.time()-start_time))
#     #
#     # # 多进程
#     # with ProcessPoolExecutor(3) as executor:
#     #     all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
#     #     start_time = time.time()
#     #     for future in as_completed(all_task):
#     #         data = future.result()
#     #         print("exe {} data".format(data))
#     #
#     #     print("last time is : {}".format(time.time()-start_time))

    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe {} data".format(data))

        print("last time is : {}".format(time.time()-start_time))