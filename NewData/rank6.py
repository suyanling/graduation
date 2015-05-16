# -*- coding: utf-8 -*-
# # 引用对集合的操作的方法
from setCollect import*
# 把ntersectName1.txt文件 和
# 各个价格区间的文件进行相交 

def getFileList(path):
    num = 1
    while True:
        if num > 11:
            break
        tmpfile = file(path + "w_" + str(num) + ".txt", 'r')
        # print tmpfile
        tmpnew = file(path + "w_P" + str(num) + ".txt", 'w')
        fp = file('/home/susu/Desktop/NewData/intersectName.txt', 'r')
        tmpCo1, tmpCo2 = collections(fp, tmpfile)
        tmpInter = intersect(tmpCo1, tmpCo2)
        tmpStr = setStr(tmpInter)
        # print tmpStr
        tmpnew.write(tmpStr)
        num = num + 1


getFileList('/home/susu/Desktop/NewData/crawler/')