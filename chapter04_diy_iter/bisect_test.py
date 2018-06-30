import bisect
from collections import deque
# 用来维持已排序的序列
# 二分查找法
inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)
print(bisect.bisect(inter_list, 3))
print(bisect.bisect_left(inter_list, 3))