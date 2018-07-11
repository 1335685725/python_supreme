# 利用两个栈stack(LIFO)实现一个队列queen(FIFO)

from inspect import stack

class MyQueue:
    def __init__(self):
        '''
        s1是lifo的
        依次s1压入s2, 那么s2对于s1来讲就是FIFO的
        '''
        self.s1 = stack()
        self.s2 = stack()

    def push(self, value):
        # 如果数据都在s2, 就将数据都压入s1, 在添加
        if self.s2 and not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
            self.s1.append(value)
        self.s1.append(value)


    def pop(self):
        # 如果都在s1, 就先将s1的元素都压入s2,在拿出来
        if self.s1 and not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        # 如果都在s2, 直接拿出来
        return self.s2.pop()

