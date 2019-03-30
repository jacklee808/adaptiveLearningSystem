# encoding=utf8 
import time
import threading

import remind
import rw

def maxNum(filename):
    f = open(filename, encoding='utf8')
    count = 0
    maxnum = 0
  
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        if count > 0:
            num = int(line[line.rfind('【') + 1:-1]) 
            if num > maxnum:
                maxnum = num
                
        count = count + 1
    print(maxnum)            
    f.close()

def getTime(list0):
    dict0 = {}
    for a in list0:
        arr = a.split(' ')
        dict0[arr[0]] = int(arr[6])
    return dict0

bTime = 25 * 60 / 500
mTime = 35 * 60 / 300
eTime = 30 * 60 / 500

def remindMe(list0, dict0):
    global dict2
    t = int(time.time())
    maxnum = 0
    dict1 = {}
    for key in dict2:
        t2 = t - dict2[key]
        if t2 >= bTime and t2 <= mTime:
            if maxnum < t2:
                maxnum = t2
            dict1[key] = t2
    if eTime - maxnum <= 0:
        remind.remind(dict1, list0, dict0)

def printCMD():
    print('b.\t返回上一层')
    print('a.\t增加内容')
    print('d.\t删除内容')
    print('m.\t修改内容')
    print('e.\t退出')
    print('-------------------')

def update(list3, list2):
    list2 = rw.updateInfo(list3, list2)
    dict2 = getTime(list2)
    rw.writeFile(filename2, list2)
    return dict2

def show(filename1, filename2):
    list0, dict0 = rw.loadData(filename1)
    list2 = rw.loadInfo(filename2)
    global dict2
    dict2 = getTime(list2)
    layer = 0
    uplayerBeginline = 0
    sameLayer = False
    while True:
        count = 0
        count2 = 0
        list3 = [0]
        begin = False
        
        for a in list0:
            c = a.count('	')
            a = a.strip()
            if begin and c < layer:
                uplayerBeginline = list3[0]
                break
            if c < layer - 1:
                sameLayer = False
            if c == layer - 1 and sameLayer == False:
                list3[0] = count
                sameLayer = True
            if c == layer and count >= uplayerBeginline:
                begin = True
                if count2 == 0:
                    printCMD()
                count2 = count2 + 1                      
                print(str(count2) + '.\t' + a[:a.find('【')])
                list3.append(count)
            count = count + 1
                
        dict2 = update(list3, list2)
        remindMe(list0, dict0)
        num = input("请输入：")
        while num != 'a' and num != 'b' and num != 'd' and num !='e' and num !='m' and (num > '9' or num < '1'):
            num = input("请输入：")
        if num == 'e':
            return
        elif num == 'b':
            num = 0
            layer = layer - 1
        elif num.isdigit():
            num = int(num)
            if num == -1:
                break
            layer = layer + 1
            
        uplayerBeginline = list3[num]
        
    return list3

filename1 = '2020.txt'
filename2 = '2020-2.txt'
dict2 = {}

rw.initInfo(filename1, filename2)
show(filename1, filename2)
