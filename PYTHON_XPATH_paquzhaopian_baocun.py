# 多进程的库

from multiprocessing import Process
from random import randint
from time import time, sleep
import os
import requests
from lxml import etree
def baocun(url):#此方法是将图片保存文件到本地 只需要传入图片地址
    try:
        root = "D://PYTHON//"#这是根文件所在
        path=root+url.split('/')[-1]#通过’/‘把图片的url分开找到最后的那个就是带.jpg的保存起来

        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:#模式以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等
                f.write(r.content)#r.content返回二进制，像图片
                print('爬取成功')
    except Exception as e:
        print(e)
def download_task(num1,num2):
    print(num1,num2)
    for i in range(num1,num2+1):
        url = 'http://op.hanhande.net/shtml/op_wz/list_2602_'+str(i)+'.shtml'
        response = requests.get(url)
        response.encoding = 'gbk'
        wb_data = response.text
        html = etree.HTML(wb_data)
        html_data = html.xpath('//*[@id="main"]/div[2]/div[2]/ul/li/a/img/@src')
        for i_ in html_data:
            print(i_)
            baocun(i_)


            # q = i_.split('/')[-1]
            # w = q.split('.')[0]
            # print(w)
            # # file = 'D:/PYTHON/%s.txt'%w
            # # a = open(file,'w',encoding='gbk')
            # # a.close()
            

def main():

    start = time()
    # 开启两个多进程，     函数名              传递的参数,需要注意的是,它接受的是一个元组(tuple)
    p1 = Process(target=download_task, args=(1,5))
    p2 = Process(target=download_task, args=(6,10))
    # 获取进程号

    # 启动进程
    p1.start()
    p2.start()

    ##############
    # 进程阻塞.
    p1.join()
    p2.join()
    ##############
    end = time()
    print(end - start)


if __name__ == '__main__':
    main()
