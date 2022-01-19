import os
def file_name(path):
    L=['周永**','韩*','任**','赵**','邹*','陈*','陈**','代**','马**','胡**','何*','靳**','库**','李**','林*','牛**','彭**','苏**','孙**','吴**','王**','王*','司*','杨*','张*','邹**','崔**','梁**']
    list=os.listdir(path)
    count =0
    for key in L:
        flag = 0
        for name in list:
            if key in name:
               flag = 1
        if flag:
            print(key,"已交")
            count = count + 1
        else:
            print(key,"就是他没交作业！！！！！————————————————————————")      
    print(count,'/',int(len(L)))     
#file_name('C:\Users\zouqi\Desktop\通信工程3班EDA实验一') 

#cPath = "C:/Users/zouqi/Desktop/通信工程3班EDA实验一"

#cPath = 'C:/Users/zouqi/Desktop/eda4'
cPath = 'C:/Users/zouqi/Desktop/通信原理实验'
cPath = 'C:/Users/zouqi/Desktop/2018级通信工程3班离校申请表'
print(cPath)
file_name(cPath)
''' 要点：
        1.  os.listdir(path) 将path路径下的所有文件名字（名字+拓展名）提取出来，放到list里
        2.  判断B字符串里面是否有A字符串： result = A in B
        3.  flag标识的运用'''
