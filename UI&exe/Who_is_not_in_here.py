from tkinter import *  
import tkinter.filedialog as tkFD
from tkinter import messagebox
import os
import pandas as pd
#程序框图大小
e_x = 500
e_y = 600
#字体
f_h = 20
f_w = 50
#矩形
bbox = 60
init_p = (70-bbox)/2
path_name = ""
path_file=""
list = [] #名字列表
list_flag = [] #保留结果
def info():
    # 弹出对话框
    messagebox.showinfo(title = '欢迎使用！',message='内容：\n    python小白花了四小时写的小程序，\n    希望能给广大班委们解决\n    谁没有交作业的问题\n    ~~~///(^v^)\\\~~~')
def getway1():
    global path_name
    path_name = tkFD.askopenfilename()
    text1.set(path_name)
def getway():
    global path_file
    path_file = tkFD.askdirectory()
    text.set(path_file)

def cha_draw(x,y):
    p_x = init_p+x*70
    p_y = init_p+y*70
    C.create_line( p_x,p_y,p_x+bbox,p_y+bbox,fill="red",width='5')
    C.create_line( p_x+bbox,p_y,p_x,p_y+bbox,fill="red",width='5')
def file_name():
    x = 0
    file_list=os.listdir(path_file)
    for key in list:
        flag = 0
        for name in file_list:
            if key in name:
                flag = 1
        if flag == 0:
            cha_draw(int(x%7),int(x/7))
        x = x+1
    

def name_show(x,y,text):
    p_x = init_p+x*70
    p_y = init_p+y*70
    C.create_rectangle( p_x,p_y,p_x+bbox,p_y+bbox,fill="yellow")
    label = Label(C, text=text,background='white',font=('Arial',13))
    #将Label放置到坐上点在Canvas的纵横30%的处
    label.place( height=f_h, width=f_w,relx= (70*x+(70-f_w)/2)/490, rely=(70*y+(70-f_h)/2)/490)
def name_read():
    f = open(path_name,'r',encoding='utf-8')
    s = f.read()
    n = ""

    count = 0
    for i in s:
        if i =='\n':
            list.append(n)
            count = 0
            n = ""
        else:
            count = count + 1
            n=n+str(i)
def name_ok():
    name_read()
    f = 0
    for j in range(0,7):
        for i in range(0,7):
            if f<len(list):
                s = list[f]
            else:
                s = 'NULL'
            f =f + 1
            name_show(i,j,s)

#D:/ALL/工作类/班级工作/18通信3班文件/name.txt
if __name__=='__main__':
    window = Tk()
    window.title('到底是谁没有交作业 v1.0')
    size = str(e_x)+'x'+str(e_y)
    window.geometry(size)
    wel = Label(
        window,
        text='欢迎使用小程序',
        bg='#2C9AE9',
        font=('Arial',12),
        width=15,height=2
    )
    
    wel.place(height=25, width=500,relx= 0, rely=0)
    fi = Label(
        window,
        text='(tips:导入名字库建议将\'\'名字们\'\'复制到txt，并以换行分隔开)',
        bg='#2C9AE9',
        font=('Arial',10),
        width=15,height=2
    )
    fi.place(height=20, width=500,relx= 0, rely=0.967)
#第一栏，导入姓名库
    tip11 = Label(
        window,
        bg='#2C9AE9',
        text='导入姓名库（请输入 or 选择路径）：',
        font=('Arial',10),
        width=15,height=12
    )
    tip11.place(height=25, width=214,relx=0, rely=0.05)

    text1 = StringVar()
    en1 = Entry(window,bd=2,width=25,textvariable=text1)
    text1.set("")
    en1.place(height=25, width=150,relx= 0.43, rely=0.05)
    
    bt1 = Button(window,text='选择路径',width=10,command=getway1)
    bt1.place(height=25, width=60,relx= 0.73, rely=0.05)
    bt12 = Button(window,text='确认',width=10,command=name_ok)
    bt12.place(height=25, width=60,relx= 0.86, rely=0.05)

#第二栏，导入文件夹
    tip1 = Label(
        window,
        bg='#2C9AE9',
        text='导入文件夹（请输入 or 选择路径）：',
        font=('Arial',10),
        width=15,height=12
    )
    tip1.place(height=25, width=214,relx=0, rely=0.1)

    text = StringVar()
    en = Entry(window,bd=2,width=25,textvariable=text)
    text.set("")
    en.place(height=25, width=150,relx= 0.43,rely=0.1)
    
    bt = Button(window,text='选择路径',width=10,command=getway)
    bt.place(height=25, width=60,relx= 0.73, rely=0.1)
    bt2 = Button(window,text='确认',width=10,command=file_name)
    bt2.place(height=25, width=60,relx= 0.86, rely=0.1)

    C = Canvas(window, bg="white")
    C.place( height=490, width=490,relx= 5/500, rely=0.15)

    info()
    #控制窗口大小，不允许修改
    window.resizable(False,False)
    window.mainloop()