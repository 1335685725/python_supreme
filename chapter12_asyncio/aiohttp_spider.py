# asyncio 爬虫, 去重, 入库
import aiohttp
import re
import asyncio
import aiomysql
from pyquery import PyQuery


start_url = "http://www.jobbole.com/"
waiting_urls = []
seen_urls = set()
stopping = False
sem = asyncio.Semaphore(3)

async def fetch(url, session):
    async with sem:
        await asyncio.sleep(1)
        try:
            async with session.get(url) as resp:
                print(f"url status : {resp.status}")
                if resp.status in [200, 201]:
                    data = await resp.text()
                    # print(data)
                    return data
        except Exception as e :
            print(e)

def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waiting_urls.append(url)
    return urls

async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handle(url, session, pool):
    # 获取文章详情, 并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    print(title)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = "insert into article_test(title) value ('{}')".format(title)
            await cur.execute(insert_sql)



async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.2)
                continue
            url = waiting_urls.pop()
            print(f"start get url: {url}")
            if re.match(r"http://.*?jobble.com/\d+/", url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handle(url, session, pool))
                    await asyncio.sleep(1)
                else:
                    if url not in seen_urls:
                        asyncio.ensure_future(init_urls(url, session))



async def main(loop):
    # 等待mysql连接建立完成
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
                                      user="root", password="",
                                      db="aiomysql_test", loop=loop, charset="utf8",
                                      autocommit=True)
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()