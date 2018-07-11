from datetime import datetime, date
import numbers

class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0 :
            raise ValueError("positive value need")
        self.value = value

    def __delete__(self, instance):
        pass

class NonDataIntField:
    # 非数据描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()
    # age = NonDataIntField()
'''
如果user是某一个类的实例, 那么user.age(以及等价的getattr(user, "age"))
首先调用__getattribute__.如果类定义了__getattr__方法, 那么在__getattribute__抛出AttributeError的时候
就会调永__getattr__,而对于描述符(__get__)的调用, 则发生在__getattribute__内部的.
user = User(), 那么user.age顺序如下 
(1)如果"age"出现在User或其基类的__dict__中, 且age是data descriptor, 那么调用其__get__方法,否则

(2)如果"age"出现在user的__dict__中, 那么直接返回obj.__dict__["age"], 否则

(3)如果"age"出现在User或其基类的__dict__中

(3.1) 如果age是non-data descriptor, 那么调用__get__方法 否则

(3.2) 返回__dict__["age"]

(4) 如果User还有__getattr__方法, 调用__getattr__方法, 否则

(5) 抛出AttributeError

'''
# "假设user对应数据库中的一张表"
# class User:
#     def __init__(self, name: str, email, birthday: date):
#         self.name = name
#         self.email = email
#         self.birthday = birthday
#         self._age = 0
#
#     def get_age(self):
#         return datetime.now().year - self.birthday.year
#
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#     @age.setter
#     def age(self, value):
#         # 检查是否是字符串类型
#         self._age = value

# 逻辑代码尽量写在main中, 如果写在外面, 别的文件import这个文件时就会执行
if __name__ == '__main__':
    # user = User("bo1", date(year=1997, month=5, day=11))
    user = User()
    # user.age = 11
    user.__dict__["age"] = 11
    print(user.__dict__) # 进入了属性描述符类中
    # print(user.age)
    # print(getattr(user, "age"))