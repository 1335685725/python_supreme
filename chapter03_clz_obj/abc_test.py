class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["bo1", "bo2"])
print(hasattr(company, "__len__"))

from collections.abc import Sized
print(isinstance(company, Sized))

#强制某些子类必须实现某些方法
# 实现一个web框架， 集成cache(redis, cache, memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 模拟抽象基类
import abc
from collections.abc import *
class CacheBase(metaclass=abc.ABCMeta):

    # 强制某些子类必须实现某些方法 Abstract Base Classes模块
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    pass


# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError
#         # return 0
#
# class RedisCache(CacheBase):
#     pass
#
#
redis_cache = RedisCache()
redis_cache.set(key="key", value="value")
