# -*- coding: utf-8 -*-
# # 引用对集合的操作的方法
from setCollect import*
# 给各个文件加上相应的属性及相应的vaule值

# 把要添加属性和value的文件中的产品的名字放到一个dict中
# 也就是file To dict
def fileDict(fp):
    dictinfo = {}
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fp.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        dictinfo[lineList[0]] = "0"
    return dictinfo


# 加上相应的属性及相应的vaule值
def addValue(fs, fp):
    dictinfo = fileDict(fs)
    tmpList = []
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fp.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        if lineList[0] in dictinfo:
            try:
                tmpstr = lineList[0] + '         '+lineList[1] + '         '+lineList[2]
                tmpList.append(tmpstr)
            except Exception, e:
            	    print e
    return tmpList

# 批量处理文件


def getFileList(path):
    num = 1
    while True:
        if num > 11:
            break
        f1 = file('/home/susu/Desktop/NewData/property/NFV_Big_1.txt', 'r')
        fileS = file(path + "w_PV" + str(num) + ".txt", 'r')
        # print fileS
        fileD = file(path + "w_PVP" + str(num) + ".txt", 'w')
        infoList = addValue(fileS, f1)
        # print info
        fileD.write('\n'.join(infoList))
        num = num + 1
        # 好习惯 关闭已经处理完的文件
        f1.close()
        fileS.close()
        fileD.close()


getFileList('/home/susu/Desktop/NewData/crawler/')

# 总的文件 total.txt是测试文件正确名字和其相应的大属性的value值
ftotalS1 = file(
    '/home/susu/Desktop/NewData/intersectName.txt', 'r')
ftotalS2 = file(
    '/home/susu/Desktop/NewData/property/NFV_Big_1.txt', 'r')
ftotalD = file('/home/susu/Desktop/NewData/total_p.txt', 'w')

info = addValue(ftotalS1, ftotalS2)
ftotalD.write('\n'.join(info))
