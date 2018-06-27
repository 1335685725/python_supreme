a = 1
b = "abc"
print(type(1))
print(type(int))
print(type(b))
print(type(str))

print("--------------------------")


class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))

print("--------------------------")

'''类是由type生成的， object是所有类都要继承的基类,是最顶层的类
type 也是一个类， 同时也是一个对象'''