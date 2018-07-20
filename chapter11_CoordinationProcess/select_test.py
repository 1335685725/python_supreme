# epoll并不一定比select好
# 在并发高的情况下,连接活跃度不是很高,epoll比select好
# 并发性不高, 连接活跃, select比epoll好

# 通过非阻塞io实现http请求

import socket
from urllib.parse import urlparse

# 使用非阻塞io完成http请求
def get_url(url):
    # 通过socket请求HTML
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
        # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    # 不停的询问连接是否建立好, 需要while不停地检测状态
    # 做计算任务或者再次请求发起其他的连接请求
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
            break
        except OSError:
            pass
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == '__main__':
    get_url("http://www.baidu.com")
