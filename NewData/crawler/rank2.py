# -*- coding: utf-8 -*-
# 把所有价格区间文件合成一个大的文件A
fa = file('A.txt', 'w+')


def add(fs, fd):
    # lines是一个list
    lines = fs.readlines()
    # lines转换成str
    lines = ''.join(lines)
    fd.write(lines)


def getFileList(path):
    num = 1
    while True:
        if num > 11:
            break
        fs = file(path + "w_" + str(num) + ".txt", 'r')
        add(fs, fa)
        fs.close()
        num = num + 1
        # 好习惯 关闭已经处理完的文件

        # fa.close()


getFileList('/home/susu/Desktop/NewData/crawler/')
fa.close()

# 给大文件A去重


def unique(fs, fd):
    tmpList = []
    while True:
        line = fs.readline()
        if len(line) == 0:
            break
        tmpList.append(line)
    tmpList = list(set(tmpList))
    fd.write(''.join(tmpList))

fA = file('A.txt', 'r')
fA1 = file('A1.txt', 'w')
unique(fA, fA1)
