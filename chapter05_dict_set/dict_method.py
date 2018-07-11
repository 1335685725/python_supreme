import copy


a = {"boo1": {"company": "iiii"},
     "boo2": {"company": "iiii"},
     }
# 清空
# a.clear()
# print(a)

# copy 返回浅拷贝
new_dict = a.copy()
new_dict["boo1"]["company"] = "ii"
print(a)
print("--------------------------")

# 深拷贝
new_dict = copy.deepcopy(a)
new_dict["boo1"]["company"] = "ii"
print(a)
print("--------------------------")

# formkeys
new_list = ["a", "b", "c"]
new_dict = dict.fromkeys(new_list, {"name": "ben"})
print(new_dict)
print("--------------------------")

# get
value = new_dict.get("ben", {})
print(value)
print("--------------------------")

# items
for k, v in new_dict.items():
    print(k, v)
print("--------------------------")


# popitem
value = new_dict.popitem()
print(value)
value = new_dict.popitem()
print(value)
value = new_dict.popitem()
print(value)
print("--------------------------")

# setdefault
default_value = new_dict.setdefault("d", "benlyons")
print("--------------------------")

# update
new_dict.update({"boddy": "im"})
new_dict.update(boddy=1, boddy2=2)
new_dict.update(("abc", "ddd"))
# 可迭代对象都可以
pass









