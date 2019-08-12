
"""
http://www.quanben.io/n/guantiwanzhengban/list.html

1. 开启两个进程 master, worker1
2. master 去爬取该页面的所有连接
3. worker1 爬取页面详细存入本地(可以考虑进程锁)
"""

"""
开多进程...
在2209个文件中检索关键字为"美丽,帅哥."
"""

import multiprocessing
from random import randint
from time import time, sleep
import os
import requests
from lxml import etree
import time
import multiprocessing


def dict_1():
    url = 'http://www.quanben.io/n/guantiwanzhengban/list.html'
    dict_ = {}
    response = requests.get(url)
    response.encoding='gbk'
    wb=response.text
    html=etree.HTML(wb)
    html_data = html.xpath('/html/body/div[3]/ul/li/a/@href')
    for i in html_data:
        q = i.split('/')[-1]
        w = q.split('.')[0]
        dict_[w]=i
    return dict_
def download_task(num1,num2,dict_):
    for i in range(num1,num2+1):
        i_ = dict_[str(i)]
        url = 'http://www.quanben.io{}'.format(i_)
        response = requests.get(url)
        response.encoding = 'utf8'
        wb_data = response.text
        html = etree.HTML(wb_data)
        html_data = html.xpath('//*[@id="content"]/p/text()')
        path = 'D://PYTHON//{}.txt'.format(str(i))
        with open(path,'w',encoding='utf8',errors='ignore') as f:
            for ii in html_data:
                f.write('\n'+ii)
            print('完成')

def main():
    dict_ = dict_1()
    download_task(1,5,dict_)
    # 开启两个多进程，     函数名              传递的参数,需要注意的是,它接受的是一个元组(tuple)
    p1 = multiprocessing.Process(target=download_task, args=(1,20,dict_))
    p2 = multiprocessing.Process(target=download_task, args=(21,40,dict_))
    # 获取进程号

    # 启动进程
    p1.start()
    p2.start()

    ##############
    # 进程阻塞.
    p1.join()
    p2.join()
    ##############




if __name__ == '__main__':
    main()
