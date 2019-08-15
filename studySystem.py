# -*- coding: utf-8 -*-
import time
import os
#
#各科规划时长（可根据时间情况调整）
times = [10080, 7200, 8640, 11520, 7200, 5760, 5760, 7200, 8640, 7200, 4320, 2880]
books = ['普通心理学', '心理学与生活', '认知心理学及其启示', '实验心理学', '组织行为学', '人格心理学', '心理与教育测量', '现代心理与教育统计学', '发展心理学', '社会心理学', '吾心可鉴', '心理学研究方法']
nandu = [0, 1, 2]
shuxidu = [0, 1, 2]
jiyishijian = [1, 24, 72, 168, 720]

def ifOthers(bianhao):
    
    if bianhao == 4 or bianhao == 13 or bianhao == 14:
        print('看本心理学吧！')
    else:
        print('给大脑来点儿新鲜的（请输入编号）：\n4. 实验心理学\n13. 英语\n14. 政治')
        bianhao = int(input())
    return bianhao

ifOthers(4)
#按进度多少排序
def getTongji():
    tj = {}
    f = open('/Users/jacklee/Documents/清华心理系学硕/各科当前学习时长.txt', 'r')
    lines = f.readlines()
    print(lines[0])
    lines = lines[1:]
    
    for line in lines:
        strs = line.split(',')
        bilv = strs[5].strip()
        tj[line] = bilv
        
    s = sorted(tj.items(),key=lambda x:x[1])
    for key, value in s:
        print(key)

getTongji()

def writeTongji(bianhao, shijian, yeshu):
    f = open('/Users/jacklee/Documents/清华心理系学硕/各科当前学习时长.txt', 'r')
    lines = f.readlines()
    f.close()
    f = open('/Users/jacklee/Documents/清华心理系学硕/各科当前学习时长.txt', 'w')
    c = 0
    for line in lines:
        if c == bianhao:
            #书名      规划时间  页数   已用时间  已看页数  当前进度比  使用时间比  进度快慢
            strs = line.split(',')
            a = int(strs[1].strip())
            b = int(strs[2].strip())
            aa = int(strs[3].strip()) + shijian
            bb = int(strs[4].strip()) + yeshu
            aaa = float('%.2f' % (aa / float(a)))
            bbb = round(bb / float(b), 2)
            if aaa < 0.0000001:
                ab = 0
            else:
                ab = round(bbb / aaa, 2)
            f.write(strs[0] + ',\t' + str(a) + ',\t' + str(b) + ',\t' + str(aa) + ',\t' + str(bb) + ',\t' + str(aaa) + ',\t' + str(bbb) + ',\t' + str(ab) + '\n')
        else:
            f.write(line)
        c = c + 1
    f.close()
    
#writeTongji(1, 100, 12)

#2019.8.15
times = [1565824800, 1565828400, 1565832000, 1565835600, 1565844600, 1565848200, 1565851800, 1565855400, 1565863800, 1565867400, 1565871000, 1565874600, 1565878200]
#提取文件夹下的地址+文件名，源文件设定排序规则
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root , file))
        return L
#print(file_name('/Users/jacklee/Documents/清华心理系学硕'))


def getRightFileTime():
    L = file_name('/Users/jacklee/Documents/清华心理系学硕/内容')
    fileTime = {}
    for file in L:
        statinfo = os.stat(file)
        #3599 3600
 #       t = (int(time.time()) - int(statinfo.st_mtime) + 3599) / 3600
        t = (int(time.time()) - int(statinfo.st_mtime) + 1) / 2
        if t == 1:
            fileTime[file] = 1
        elif t == 24:
            fileTime[file] = 2
        elif t == 72:
            fileTime[file] = 3
        elif t == 168:
            fileTime[file] = 4
        elif t == 720:
            fileTime[file] = 5
    return fileTime

def createFile():
    print('请输入编码：')
    name = input()
    print(name)
    num = (len(name) - len(name.replace('-',"")))
    index = int(name[0]) - 1
    filename = '/Users/jacklee/Documents/清华心理系学硕/内容/' + name + books[index] + '.txt'

    if num == 1:
        os.system('cp /Users/jacklee/Documents/清华心理系学硕/内容/0-0.txt ' +  filename)
    elif num == 1:
        os.system('cp /Users/jacklee/Documents/清华心理系学硕/内容/0-0-0.txt ' + filename)
    else:
        filename = ''
    return filename

createFile()
fileTime = getRightFileTime()
while True:
    for t in times:
        tt = int(time.time())
        print(tt - t + 34040)
        #if t == tt or (tt - t) % 86400 == 0:
        #if t == tt + 34040 or (tt - t + 34040) % 86400 == 0:
        if True:
            #print(tt - t)
            fileTime = getRightFileTime()
            if fileTime:
                print(fileTime)
    time.sleep(1)