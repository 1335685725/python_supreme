# python3.3中新加的yield from 语法
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bbb1": "http://projectsedu.com",
    "bbb2": "http://benlyons.com"
}

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)

def my_chain(*args, **kwargs):
    for my_iterable in args:
        # for value in my_iterable:
        #     yield value
        yield from my_iterable
for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 1.main调用方, g1(委托生成器) gen(子生成器)
# 2. yield from会在调用方与子生成器建立一个双向通道