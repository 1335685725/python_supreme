# Python中的垃圾回收的算法是采用  引用计数

a = object() # 计数为1
b = a # 再加1 等于2
del a # 减1, 等于1, 引用计数不为0, 不回收
print(b)
print(a)

class A:
    def __del__(self):
        '''
        自定义del函数, 用于当回收对象的时候释放资源
        :return:
        '''
        pass