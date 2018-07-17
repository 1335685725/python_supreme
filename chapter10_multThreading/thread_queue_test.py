# 通过queue来实现线程间的同步
from queue import Queue
from chapter10_multThreading import variable
import time
import threading

def get_detail_html(queue):
    # 抓取文章详情页
    # global detail_url_list
    while True:
        url = queue.get() # 阻塞的方法, 为空的时候回一直阻塞在这里
        print("get html detail started")
        time.sleep(2)
        print("get html detail end")

def get_detail_url(queue):
    # 爬取文章列表页
    # global detail_url_list
    detail_url_list = variable.detail_url_list
    print("get url detail started")
    time.sleep(2)
    for i in range(20):
        queue.put("http://projectsedu.com{id}".format(id=i))
    print("get url detail end")


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        thread_detail_html.start()