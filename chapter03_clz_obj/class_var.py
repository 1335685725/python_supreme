"类变量"
class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
a.aa = 1111 # 实例增加了一个aa属性
A.aa = 11
print(a.x, a.y, a.aa) # 1111
print(A.aa) # 11