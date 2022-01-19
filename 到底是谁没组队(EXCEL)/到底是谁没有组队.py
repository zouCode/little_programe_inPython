import xlrd 
cpath = 'C:/Users/zouqi/Desktop/EDA课设通信3班.xlsx'
dpath = 'D:/ALL/工作类/班级工作/18通信3班文件/18通信3班信息表.xlsx'
#读取标准名单
x = xlrd.open_workbook(dpath)
table0 = x.sheets()[0]
name_list =[]
for i in range (1,30):
    charr = table0.cell(i,1).value
    if charr=='姜致远':
        continue
    if charr=='':
        break
    else:
        name_list.append(charr)
#读取待检测文件名单
xl = xlrd.open_workbook(cpath)
table = xl.sheets()[0]
name = []
row = table.col_values(0)
row = len(row)
for i in range(3,row):
    for j in range(1,3):
        charr = table.cell(i,j).value
        if charr=='':
            if j==1:
                break
            else:
                charr='空'
        name.append(charr)
name_result = []
count = 0
for key in name_list:
    flag=0
    for key2 in name:
        if key==key2:
            flag=1
    if flag==1:
        name_result.append(key)
        count = count + 1
    else:
        name_result.append(key+str('(未登记)'))
print(name_result)
print('完成情况：'+str(count)+'/'+str(len(name_list)))


    