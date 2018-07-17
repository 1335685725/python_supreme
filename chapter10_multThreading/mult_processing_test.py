# import os
# # 新建一个子进程, 只能用在Linux/Unix上
# pid = os.fork()
#
# print("bbb")
# if pid == 0 :
#     print("子进程 {}, 父进程: {}".format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程 {}:".format(pid))
# time.sleep(2)

import time
import multiprocessing
# 多进程编程
def get_html(n):
    time.sleep(n)
    print("sub progress success")
    return n

class MyProgress(multiprocessing.Process):
    def run(self):
        pass

if __name__ == '__main__':
    progress = multiprocessing.Process(target=get_html, args=(2, ))
    print(progress.pid)
    progress.start()
    print(progress.pid)
    progress.join()
    print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))

    # 等待所有任务完成
    pool.close()
    # 先关闭池, 不让进程进来
    pool.join()
    # 获取到值
    print(result.get())

    for result in pool.imap(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))