file_path ='D:\day01\kaifangX.txt'
file = 'C:/Users/刘钰/Desktop/test.txt'
a = open(file,'w',encoding='gbk')

with open(file_path,'r',encoding='gbk',errors='ignore') as f:
    for i in range(10000):
        try:
            emile=f.readline().split(',')[9]
            a.write(emile)
        except Exception as e:
                 print('空行')
a.close()