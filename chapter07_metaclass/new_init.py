import _collections_abc # 接口的实现
import collections # 接口
import _collections # 某些数据结构的接口
import collections.abc # 抽象基类
class User:
    def __new__(cls, *args, **kwargs):
        '''
        在init之前
        :param args:
        :param kwargs:
        :return:
        '''
        print("in new")
        # return super().__new__(cls)

    def __init__(self, name):
        print("in init")
        self.name = name
# new是用来控制对象生成过程, 在对象生成之前
# init用来完善对象的
#如果new方法不返回对象, 则不会调用init方法

if __name__ == '__main__':
    user = User(name="ben")
    pass