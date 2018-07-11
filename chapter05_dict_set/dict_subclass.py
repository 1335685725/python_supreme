# 不建议继承list, dict
# dict是C语言实现的, 某些情况下就算覆盖了父类的方法, 也不会去调用
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

my_dict = Mydict(one=1) # 不生效
my_dict["one"] = 1 # 生效
# print(my_dict)

# 推荐继承UserDict
from collections import UserDict

class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

my_dict = Mydict(one=1) # 不生效
# my_dict["one"] = 1 # 生效
print(my_dict)


#defaultdict
from collections import defaultdict

my_dict = defaultdict(dict)
my_value = my_dict["body"]
pass