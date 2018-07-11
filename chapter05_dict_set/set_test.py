# set 集合 fronzenset(不可变集合), 无序, 不重复

s = set('abcddd')
print(s)
# s = set(["a", "b", "c"])
# print(s)
s = {'a', 'b'}
print(type(s))
print("-----------------------------")

# fronzenset
fs = frozenset("abcdddee") # 一旦设置好就不可变, 可以作为dict的key
print(s)
print("-----------------------------")

# 向set添加数据
another_set = set("sddf")
s.update(fs)
print(s)

re_set = s.difference(another_set)
print(re_set)
# 集合运算
# 性能很高 hash算法, 时间复杂度为1
re_set = s - another_set # 求差集
re_set = s & another_set # 求合集
re_set = s | another_set # 求并集

if "c" in s:
    print("yes")

# 子集
print(s.issubset(re_set))