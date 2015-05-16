# -*- coding: utf-8 -*-

# 给爬取到的文件去重


def unique(f):
    lines = f.readlines()
    # 用set()函数去重
    line = set(lines)
    # line.sort()
    return ''.join(line)

# 批量处理文件


def getFileList(path):
    num = 1
    while True:
        if num > 11:
            break
        fileS = file(path + "w" + str(num) + ".txt", 'r')
        # print fileS
        fileD = file(path + "w_" + str(num) + ".txt", 'w')
        fileD.write(unique(fileS))
        fileS.close()
        fileD.close()
        num = num + 1
        # 好习惯 关闭已经处理完的文件


getFileList('/home/susu/Desktop/NewData/crawler/')
