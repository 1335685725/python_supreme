import threading
from threading import Lock, RLock
# RLock 可重入锁, 可以连续调用acquire, 一定要注意acquire和release的次数一定要相等


total = 0
lock = Lock()
def add(lock):
    global total
    for i in range(1000000):
        lock.acquire()
        total +=1
        lock.release()
def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -=1
        lock.release()
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
# 用锁会影响性能, 锁会引起死锁

def add1(a):
    a+=1

def desc1(a):
    a-=1

'''
1.load a
2. load 1
3. +
4. 赋值给a
'''

import dis
print(dis.dis(add1))
print(dis.dis(desc1))









