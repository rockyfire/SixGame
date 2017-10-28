# coding :utf-8
import queue
import threading
import json
import time
import codecs
import requests
import random
from bs4 import BeautifulSoup
from lxml import etree

# 2.0    ---------------------------

class MutliThreadCrawl(threading.Thread):
    def __init__(self,url,queue,out_queue):
        threading.Thread.__init__(self)
        self.url=url
        self.queue=queue
        self.out_queue=out_queue

    def run(self):
        while True:
            # 变换年份 ==>> 不同的URL
            year=self.queue.get()
            # print (year)
            url =self.url+str(year)
            req = requests.get(url=url)
            self._parser_html(req.text)
            # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
            self.queue.task_done()

    def _parser_html(self,content):
        soup = BeautifulSoup(content, 'html.parser')
        data = []
        for i in soup.find_all("tr"):
            tr=[]
            for j in i.find_all("td"):
                if str(j.string) == "None":
                    for m in j.find_all('span',attrs={"class":"lhcs"}):
                        tr.append(str(m.string))
                else:
                    tr.append(str(j.string))
            data.append(tr)
        if len(data) != 0:
            # 数据队列
            self.out_queue.put(data)

class ThreadWriteFile(threading.Thread):
    def __init__(self, queue, lock, f):
        threading.Thread.__init__(self)
        # data_queue > queue
        self.queue = queue
        self.lock = lock
        self.f = f

    def run(self):
        while True:
            item = self.queue.get()
            self._parse_data(item)
            self.queue.task_done()

    def _parse_data(self, item):
        for i in item:
            # 上锁
            with self.lock:
                # self.write(",".join(i)+"\n")
                # windows
                self.f.write(",".join(i)+"\n\r")


# 线程锁
lock = threading.Lock()
# URL队列
urls_queue = queue.Queue()
# 数据队列
data_queue = queue.Queue()
# 用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
# f=codecs.open("out.txt","w+","utf8")
f=codecs.open("out.csv","w+","utf8")


if __name__ == "__main__":

    url = 'http://6hc.98vp.com/lhc/gethistory?y='
    for i in range(1976,2018):
        urls_queue.put(i)

    for i in range(4):
        t=MutliThreadCrawl(url,urls_queue,data_queue)
        t.setDaemon(True)
        t.start()
    for i in range(4):
        t=ThreadWriteFile(data_queue,lock,f)
        t.setDaemon
        t.start()

    urls_queue.join()
    data_queue.join()

    with lock:
        f.close()
