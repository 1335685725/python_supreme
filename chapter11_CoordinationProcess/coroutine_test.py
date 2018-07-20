# 1. 回调模式编码复杂度高
# 2. 同步编程并发性不高
# 3. 多线程编程需要线程间同步, lock
#
# 1. 采用同步的方法去编写异步的代码
# 2. 采用单线程去切换任务
#       1. 线程是由操作系统切换的,单线程切换意味着需要程序员自己去调度任务
#       2. 不再需要锁, 并发性高, 如果单线程内切换函数, 性能远高于线程切换, 并发性高

# def get_url(url):
#     # do something 1
#     html = get_html(url) # 此处暂停, 切换到另一个函数
#     # parse html
#     # urls = parse_url(html)
#
# def get_url2():
#     pass
# 传统函数过程: A->B->C
# 我们需要一个暂停的函数, 可以在适当的时候恢复函数的执行
# 出现了协程 -> 有多个入口的函数, 可以暂停的函数(可以在暂停的地方传入值)

def gen_func():
    # 可以产生值, 可以接受值
    html = yield 1
    print(html)
    yield 2
    yield 3
    return "bbb"

# 生成器不仅可以产生值, 还可以接受值

if __name__ == '__main__':
    gen = gen_func()
    # 启动有两种方式 next(), send
    # 在调用send发送非None值时,我们必须启动一次生成器, 方式有两种,1.send(None) 2. next()
    url = next(gen)
    html = "bbb"
    gen.send(html)# send方法可以传递值进入生成器内部,同时还可以重启生成器执行到下一个yield
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))