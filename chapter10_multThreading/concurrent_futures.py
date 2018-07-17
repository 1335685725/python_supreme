from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED
from concurrent.futures import Future

# 未来对象, task返回容器

# 线程池, 为什么要用到线程池
# 主线程可以获取到某一个线程的状态或者某一个任务的状态, 以及返回值
# 当一个线程完成时,我们主线程可以立即知道
# futures可以让多线程和多进程编码接口一致

import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

excutor = ThreadPoolExecutor(max_workers=1)
# 用submit函数提交执行的函数到线程池中, submit立即返回
# task1 = excutor.submit(get_html, 2)
# task2 = excutor.submit(get_html, 3)

# 要获取已经成功的task的返回, 谁先完成就处理谁
urls = [3, 2, 4]
all_task = [excutor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=ALL_COMPLETED)
print("completed")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

# 通过executor获取已经完成的task, 返回顺序是一致的
# for data in excutor.map(get_html, urls):
#     print("get {} page success".format(data))


# # 判断任务是否完成
# print(task1.done())
# 取消任务, 当任务已经在执行或者执行完成时返回False
# print(task2.cancel())
# # 执行结果
# print(task1.result())
