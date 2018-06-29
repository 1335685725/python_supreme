# class A:
#     name = "A"
#     def __init__(self):
#         self.name = "obj"
#
#
# a = A()
# print(a.name)
# '''由下而上查找属性, 先找对象的, 再找类'''
# 新式类
class E:
    pass


class D:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass

print(A.__mro__)