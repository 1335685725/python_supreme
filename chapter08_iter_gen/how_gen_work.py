# 1.Python中函数的工作原理
'''

'''
import inspect
frame = None
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

# python.exe会用一个PyEval_EvalFramEx(c函数)去执行foo()函数首先创建一个栈帧
'''
python 一切皆对象, 栈帧对象,字节码对象
当foo调用子函数bar时, 又会创建一个栈帧
所有的栈帧都是分配在堆内存中,这就决定了栈帧可以独立于调用者存在
'''
import dis
# print(dis.dis(foo))

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

def gen_func():
    yield 1
    name = "ben"
    yield 2
    age = 17
    return "immc"

gen = gen_func()
print(dis.dis(gen_func))

print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

from collections import UserList