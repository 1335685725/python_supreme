# 生成器函数: 函数内有yield关键字
def gun_fun():
    yield 1
    yield 2
# 惰性求值, 延时求值
# 斐波那契 0 1 1 2 3 5 8
def fib(index):
    if index <= 2:
        return 2
    else:
        return fib(index-1) + fib(index-2)

def fib2(index):
    a,b,n = 0, 1, 0
    while n < index:
        yield b
        a,b = b, a+b
        n +=1

for i in fib2(10):
    print(i)


def fun():
    return 1
if __name__ == '__main__':
    # 生成器对象:Python编译字节码时就已经产生了
    gen = gun_fun()
    for value in gen:
        print(value)
    res = fun()
    pass