# 容器序列: tuple, list, deque 可以放置任意类型的序列
# 扁平序列: str, bytes, bytearray, array.array 只能放置同一类型的数据
# 可变序列: list, deque, bytearray, array
# 不可变序列: tuple, str, bytes

mylist = []
mylist.append(1)
mylist.append("a")

import _collections_abc
from collections import abc

# + # 只能+list
a = [1, 2]
c = a + [3, 4]
print(c)

# += 可以是任意序列类型 +=是使用的__iadd__, 也就是extend(for循环append)方法
a += (3, 4)
print(a)
# 也就是说append添加任何序列类型
a.append((1, 2))