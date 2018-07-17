import threading
import time
from chapter10_multThreading import variable

detail_url_list = []

def get_detail_html():
    # 抓取文章详情页
    # global detail_url_list
    detail_url_list = variable.detail_url_list
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get html detail started")
            time.sleep(2)
            print("get html detail end")

def get_detail_url():
    # 爬取文章列表页
    # global detail_url_list
    detail_url_list = variable.detail_url_list
    print("get url detail started")
    time.sleep(2)
    for i in range(20):
        detail_url_list.append("http://projectsedu.com{id}".format(id=i))
    print("get url detail end")


    if __name__ == '__main__':
        thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
        thread_detail_url.start()
        for i in range(10):
            thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_list,))
            thread_detail_html.start()

