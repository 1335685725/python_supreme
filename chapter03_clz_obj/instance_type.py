class A:
    pass


class B(A):
    pass


a = A()
b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print("---------------------------------------")
''':type返回的是一个类对象, type(b)指向B类对象 所以下面第一个语句返回True'''
print(type(b) is B)
print(type(b) is A)
