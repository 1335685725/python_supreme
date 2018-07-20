# 生成器是可以暂停的函数
import inspect

def gen_func():
    value = yield 1
    # 返回值给调用方, 调用方通过send方法返回值给gen
    return "bbb"

# 用同步的方式编写异步的代码, 在适当的时候暂停函数并在适当的时候启动函数
import socket
def get_socket_data():
    yield "bbb"

def download_url():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
        # 注册socket
    selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
    source = yield from get_socket_data()
    data = self.data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    self.client.close()
    urls.remove(self.spider_url)
    if not urls:
        global stop
        stop = True
def downloader_html(html):
    html = yield from downloader()

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    print(next(gen))
    print(inspect.getgeneratorstate(gen))
    try:
        print(next(gen))
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))