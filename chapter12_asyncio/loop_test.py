# 包含各种特定系统实现的模块化事件循环
# 传输和协议对象
# 对TCP, UDP, SSL, 子进程, 延时调用以及其他具体支持
# 模仿future模块但适用于事件循环的Future类
# 呼吁yield from 的协议和任务, 可以让你用顺序的方式编写并发代码
# 必须使用一个将阻塞io的调用时, 有接口将这个事件转义到线程池
# 模仿threading模块中的同步原语, 可以用作单线程内的协程之间

# 事件循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio是Python用于解决异步io编程的一整套解决方案
# tornado, gevent, twisted (scrapy, Django channels(http2.0))
# tornado(实现web服务器), django+flask(不提供web服务器)(部署用uwsgi, gunicorn + nginx)
# tornado可以直接部署, nginx+tornado

# 使用asyncio
import asyncio
import time
from functools import partial
# async def get_html(url):
#     print("start get url")
#     # time.sleep(n) 同步阻塞接口, 不能使用在协程里面
#     await asyncio.sleep(2)
#     # time.sleep(2)
#     print("end get url")
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop() # 时间循环
#     task = [get_html("http://www.imooc.com") for i in range(100)]
#     loop.run_until_complete(asyncio.wait(task))
#     print(time.time()-start_time)

# 获取协程的返回值
# async def get_html(url):
#     print("start get url")
#     # time.sleep(n) 同步阻塞接口, 不能使用在协程里面
#     await asyncio.sleep(2)
#     # time.sleep(2)
#     print("end get url")
#     return "bbb"
#
# def callback(url, future):
#     print(url)
#     print("send email to ben")
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop() # 时间循环
#     # get_future = asyncio.ensure_future(get_html("http://www.imooc.com")) # 拿到future对象
#     task = loop.create_task(get_html("http://www.imooc.com"))
#     task.add_done_callback(partial(callback, "http://www.imooc.com"))
#     loop.run_until_complete(task)
#     print(time.time()-start_time)
#     print(task.result())


# wait 和gather
async def get_html(url):
    print("start get url")
    # time.sleep(n) 同步阻塞接口, 不能使用在协程里面
    await asyncio.sleep(2)
    # time.sleep(2)
    print("end get url")

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop() # 时间循环
    # task = [get_html("http://www.imooc.com") for i in range(100)]
    # loop.run_until_complete(asyncio.gather(*task))
    # print(time.time()-start_time)
    # gather 和 wait的区别
    # gather更加high-level
    group1 = [get_html("http://www.bbbb.com") for i in range(100)]
    group2 = [get_html("http://www.aaaa.com") for i in range(100)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    group1.cancel()
    # group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time()-start_time)
