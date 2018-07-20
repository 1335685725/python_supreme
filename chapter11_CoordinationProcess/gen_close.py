def gen_func():
    # 可以产生值, 可以接受值
    try:
        yield 1
    except GeneratorExit:
        pass
    # print(html)
    # yield 2
    # yield 3
    return "bbb"

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)
