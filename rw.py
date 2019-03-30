import time

def loadData(filename):
    list0 = []
    dict0 = {}
    count = 0
    f = open(filename, encoding='utf8')

    while True:
        line = f.readline()
        if not line:
            break
        list0.append(line)
        num = line[line.rfind('【') + 1:-2]
        dict0[num] = count
        count = count + 1
            
    f.close()
    return list0, dict0

def loadInfo(filename):
    list0 = []
    f = open(filename, encoding='utf8')

    while True:
        line = f.readline()
        if not line:
            break
        list0.append(line)
           
    f.close()
    return list0

def initInfo(filename1, filename2):
    f = open(filename1, encoding='utf8')
    f2 = open(filename2, 'w', encoding='utf8')
    count = 0
#重点等级（1-3），难点等级（1-3），疑点（1-3），记忆次数,
#本次是否通过，开始学习时间，最后学习时间
    key = 0
    diffcult = 0
    doubt = 0
    rememberTimes = 0
    isOK = 0
    time1 = 0
    time2 = 0
    while True:
        line = f.readline()
        if not line:
            break
        
        line = line.strip()
        num = line[line.rfind('【') + 1:-1]
        print(num + ' ' + str(key) + ' ' + str(diffcult) + ' ' + str(doubt)
            + ' ' + str(rememberTimes) + ' ' + str(isOK) + ' ' + str(time1)
            + ' ' + str(time2), file=f2) 
        count = count + 1
            
    f.close()
    f2.close()

def updateInfo(list0, list2):
    key = 0
    diffcult = 0
    doubt = 0
    rememberTimes = 0
    isOK = 0
    time1 = 0
    time2 = 0
    num = 0
    for a in list0:
        arr = list2[a].split(' ')
        num = arr[0]
        key = int(arr[1])
        diffcult = int(arr[2])
        doubt = int(arr[3])
        rememberTimes = int(arr[4])
        isOK = int(arr[5])
        time1 = int(arr[6])
        time2 = int(time.time())
        if time1 == 0:
            time1 = time2
        list2[a] = num + ' ' + str(key) + ' ' + str(diffcult) + ' ' + str(doubt) + ' ' + str(rememberTimes) + ' ' + str(isOK) + ' ' + str(time1) + ' ' + str(time2)

    return list2

def writeFile(filename, list0):
    f = open(filename, 'w', encoding='utf8')
    for a in list0:
        if a[-1:] == '\n':
            print(a[:-1], file=f)#因print输出自带换行
        else:
            print(a, file=f)
    f.close()
