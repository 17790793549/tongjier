import csv
import re
file = 'C:/Users/刘钰/Desktop/access.log'
with open(file,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)  # 使用csv.reader读取csvfile中的文件
    file_ = 'C:/Users/刘钰/Desktop/网址.txt'
    asd = open(file_,'a',encoding='utf8')
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        q = re.findall(r"\"http(.+?)\"",row[0])
        if q !=[]:
            qwe = 'http%s/'%q[0]
            asd.write('\n'+qwe)
    asd.close()

"""
    
import csv
import re
file = 'C:/Users/刘钰/Desktop/access.log'
with open(file,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)  # 使用csv.reader读取csvfile中的文件
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        q = re.findall(r"\"http(.+?)\"",row[0])
        if q !=[]:
            qwe = 'http%s/'%q[0]
            file_ = 'C:/Users/刘钰/Desktop/网址.txt'
            with open(file_,'a',encoding='utf8') as ro:
                ro.write('\n'+qwe)




        # file_ = 'C:/Users/刘钰/Desktop/text/‪{}_{}_{}.txt'.format(row[0],row[1],row[2])
        # q = row[3]
        # with open(file_,'w',encoding='utf8') as cs:
        #     cs.write(q)
    


"""
