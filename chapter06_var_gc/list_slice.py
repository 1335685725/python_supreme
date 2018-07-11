# 列表拆分  将N个元素的列表拆分为三个一组的
from random import randint, sample, choice, shuffle
# 原始列表为
alist = [randint(0, 10) for i in range(10)]
result_list = [alist[i:i+3] for i in range(0, len(alist), 3)]
# alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(result_list)
print("----------------------------")

# 新需求来啦! 随机三个元素组成一组
# result_list = [[sample(alist, 3) for i in range(3)] for i in range(0, len(alist), 3)]
# result_list = [sample(alist, 3) for i in range(0, len(alist), 3)]
# print(result_list)
shuffle(alist)
result_list = [alist[i:i+3] for i in range(0, len(alist), 3)]
print(result_list)