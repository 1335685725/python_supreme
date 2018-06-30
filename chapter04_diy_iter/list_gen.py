# 列表推导式

# 提取1-20之间的奇数]
odd_list = []
for i in range(21):
    if i % 2 ==1:
        odd_list.append(i)
print(odd_list)

odd_list = [i for i in range(21) if i % 2 ==1]
print(odd_list)

# 逻辑复杂的情况
# 列表生成式性能高于列表操作

def hadle_item(item):
    return item * item

odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)


# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 ==1)
print(type(odd_gen))
print(odd_gen)
for i in odd_gen:
    print(i, end="  ")

odd_list = list(odd_gen)
print(odd_list)

# 字典推导式
my_dict = {"boo1": 22, "boo2": 23, "iiii": 24}
reverse_dict = {value: key for key, value in my_dict.items()}
print(reverse_dict)


# 集合推导式
# my_set = set(my_dict.keys())
my_set = {key for key in my_dict}
print(type(my_set))
print(my_set)
