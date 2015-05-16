# -*- coding: utf-8 -*-
# # 引用对集合的操作的方法
from setCollect import*
# 给各个文件加上相应的vaule值


# 一个文件打开一次只能进行一次操作
# 要重复多次操作一个文件 要把它放在循环里打开

# f1 = file('NV.txt', 'r')
# f2 = file('newP1.txt', 'r')

# f3 = file('NVP1', 'w')

#  把文件的内容转化成dict


def fileDict(fp):
    dictinfo = {}
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fp.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        dictinfo[lineList[0]] = lineList[1]
    return dictinfo


# 把dict对象转化成字符串
def dictStr(dict):
    listinfo = []
    for (k, v) in dict.items():
        tmp = k + "	" + str(v) + "\n"
        listinfo.append(tmp)
    listinfo.sort()
    return ''.join(listinfo)

# 给汽车名加相应的值


def addValue(fp, fs):
    dictinfo = fileDict(fs)
    info = {}
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fp.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        if lineList[0] in dictinfo:
            info[lineList[0]] = dictinfo[lineList[0]]
    return info

# 批量处理文件


def getFileList(path):
    num = 1
    while True:
        if num > 11:
            break
        f1 = file('/home/susu/Desktop/NewData/addNameValue', 'r')
        fileS = file(path + "w_P" + str(num) + ".txt", 'r')
        # print fileS
        fileD = file(path + "w_PV" + str(num) + ".txt", 'w')
        info = addValue(fileS, f1)
        # print info
        fileD.write(dictStr(info))
        num = num + 1
        # 好习惯 关闭已经处理完的文件
        f1.close()
        fileS.close()
        fileD.close()


getFileList('/home/susu/Desktop/NewData/crawler/')


# 总的文件 total.txt是测试文件正确名字和其相应的value值
ftotalS1 = file(
    '/home/susu/Desktop/NewData/intersectName.txt', 'r')
ftotalS2 = file(
    '/home/susu/Desktop/NewData/addNameValue', 'r')
ftotalD = file('/home/susu/Desktop/NewData/total.txt', 'w')

info = addValue(ftotalS1, ftotalS2)
ftotalD.write(dictStr(info))