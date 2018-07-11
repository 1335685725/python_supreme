# python 和java的变量不一样,
# python 中的变量本质上是一个指针, 便利贴

a = 1
a = "abc"
# 1. a贴在1上面
# 2. 先生成对象, 再贴上去

a = [1, 2, 3]
b = a
print(a is b)
print(id(a), id(b))
b.append(4)
print(b)

print("---------------------------")

a = [1, 2, 3]
b = [1, 2, 3] # 重新生成一个对象
print(id(a), id(b))
print(a is b)
print(a == b)  # 调用__contains__函数, 比较值
print("---------------------------")

class Person:
    pass

person = Person()
# if isinstance(person, Person):
# Person类也是一个对象, 全局唯一的
if type(person) is Person:
    print("yes")

# 遇上小整数小字符串时, 会在内存内部存放这个数值,
# 如果再创建一个变量值等于这个数值, 他的引用也是指向这个内存区域的

a = 1
b = 1
print(a is b)
print(id(a), id(b))