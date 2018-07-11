from datetime import date, datetime

# __getattr__, __getattribute__
# __getattr__在查找不到属性的时候调用

class User:
    def __init__(self, info={}):
        # self.name = name
        # self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        '''
        找不到属性才调用这个函数
        :param item:
        :return:
        '''
        return self.info[item]

    def __getattribute__(self, item):
        '''
        无条件先使用这个函数, 尽量不重写这个魔法方法, 一般写框架采用
        :param item:
        :return:
        '''
        return "benlyons"

if __name__ == '__main__':
    user = User(info={"company": "ben", "name": "bo1"})
    print(user.name)
    print(user.test)