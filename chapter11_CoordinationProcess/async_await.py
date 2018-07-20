# Python为了将语意变得更加明确, 就引入了async和await关键词用于定义原生的协程

from collections import Awaitable

async def downloader(url):
    return "bbb"

async def download_url(url):
    # do somethings
    html = await downloader(url)
    return html

#

if __name__ == '__main__':
    coro = downloader("http://www.imooc.com")
    coro.send(None)