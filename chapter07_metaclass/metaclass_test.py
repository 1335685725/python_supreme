# 类也是对象, type也是用来创建类的类
def create_class(name):
    if name == "user" :
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# type 动态创建类
# User = type("User", (), {"name": "ben"})

def say(self):
    return f"I am user {self.name}"

class BaseClass:
    def answer(self):
        return "I am baseclass"
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
# 什么是元类, 元类就是创建类的类, type 就是一个元类
class User(metaclass=MetaClass):
    def __init__(self, name ):
        self.name = name
    def __str__(self):
        return "user"
# python中类的实例化的过程, 会首先寻找metaclass,通过metaclass去创建User类,
# 如果没有metaclass, 去基类找metaclass, 然后去模块中找
# 最后找不到metaclass才调用type创建类对象,

if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()

    # User = type("User", (BaseClass, ), {"name": "ben", "say": say})
    my_obj = User(name="benlyons")
    print(type(my_obj))
    print(my_obj)
    # print(my_obj.say())
    # print(my_obj.answer())
    print("-"*20)

