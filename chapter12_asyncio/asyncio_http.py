# asyncio 没有提供http协议的 接口 aiohttp
import socket
from urllib.parse import urlparse
import asyncio
async def get_url(url):
    # 通过socket请求HTML
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
        # 建立连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((host, 80))
    all_lines = []
    async for raw_lines in reader:
        data = raw_lines.decode("utf8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html

async def main(loop):
    tasks = []
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(get_url(url))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
if __name__ == '__main__':
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(loop))
    print("success in {}".format(time.time() - start_time))