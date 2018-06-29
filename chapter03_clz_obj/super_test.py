class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        # super(B, self).__init__()
        super().__init__()

# 既然我们重写了B的构造函数, 为什么还要调用super?
# super的执行顺序到底是怎样的?
# super不是调用父类, 而是调用mro中的下一个类

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

from threading import Thread
class MyThread(Thread):
    def __init__(self, user, name):
        self.user = user
        # self.name = name
        super().__init__(name=name)


if __name__ == '__main__':
    print(D.__mro__)
    d = D()