
import csv
file = 'C:/Users/刘钰/Desktop/qwe.csv'
with open(file,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)  # 使用csv.reader读取csvfile中的文件

    birth_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        file_ = 'C:/Users/刘钰/Desktop/text/‪{}_{}_{}.txt'.format(row[0],row[1],row[2])
        q = row[3]
        with open(file_,'w',encoding='utf8') as cs:
            cs.write(q)
    