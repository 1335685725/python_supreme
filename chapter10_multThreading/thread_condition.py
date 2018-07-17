from threading import Condition, Lock
import threading

# 条件变量, 用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         self.lock = lock
#         super().__init__(name="xiaoAi")
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 好啊".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         self.lock = lock
#         super().__init__(name="tianMao")
#     def run(self):
#         self.lock.acquire()
#         print("{} : 小爱同学".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧".format(self.name))
#         self.lock.release()

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name="xiaoAi")
    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在".format(self.name))
            self.cond.notify()
            print("{} : 好啊".format(self.name))


class TianMao(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name="tianMao")
    def run(self):
        with self.cond:
            print("{} : 小爱同学".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 我们来对古诗吧".format(self.name))
            self.cond.release()

if __name__ == '__main__':
    cond = Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    xiaoai.start()
    tianmao.start()
# 启动顺序很重要, wait要先启动
# wait和notify一定要在with condition之后才能调用
# condition有两把锁, 底层锁会在wait的时候释放,上面的锁,会在每次调用wait时候分配一把
# 并放入到condition的等待队列中,等待notify方法的唤醒