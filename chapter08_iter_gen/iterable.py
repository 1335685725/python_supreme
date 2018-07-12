# 迭代器协议
# 迭代器是访问集合内元素的一种方法, 一般用来遍历数据
# 迭代器和以下标访问方式不一样, 迭代器是不能返回的,迭代器提供了一种惰性访问数据的方式
#[] __getitem__, 可以for循环其实就是__iter__

from collections.abc import Iterable, Iterator

a = [1, 2]
iter_rator = iter(a) # 生成器
print(iter_rator)
print(isinstance(a, Iterator)) # False
print(isinstance(a, Iterable)) # True