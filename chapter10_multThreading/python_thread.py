# 对于io操作来说,多线程和多进程性能相差不大,
# 1. 通过Thread实例化
import time
import threading

def get_detail_html(url):
    print("get html detail started")
    time.sleep(2)
    print("get html detail end")

def get_detail_url(url):
    print("get url detail started")
    time.sleep(2)
    print("get url detail end")

# 通过继承Thread实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get html detail started")
        time.sleep(2)
        print("get html detail end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get html detail started")
        time.sleep(2)
        print("get html detail end")

if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailHtml("get_detail_url")

    start_time = time.time()
    thread1.setDaemon(True) # 设置为守护线程
    thread2.setDaemon(True) # 不管这两个线程有没有运行完成, 主线程关闭后,两个线程直接退出

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()# 等到这两个线程执行完成才执行下面的代码

    end_time = time.time()
    print("time : {}".format(end_time-start_time))

