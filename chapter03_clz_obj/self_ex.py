'''Python的自省机制,通过一定的机制来查询到对象的内部结构'''

from chapter03_clz_obj.class_method import Date

class Person:
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("bbb")
    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["addr"] = "北京市"
    print(user.__dict__)
    print(user.name) # user 不是对象的属性, 向上查找找到person类对象的属性
    print(Person.__dict__)

    print(dir(user))