#!/usr/bin/python
# -*-  coding: utf-8 -*-
# 处理原文件 首先把原文件
# 2.2 <DOC2>  XXX 花冠  发动机 1
# 这样的格式转换成
# 花冠  发动机 1
# 这样的格式
# 把两个这样的原文件所以把处理后的原文件合并成一个文件

# 读取两个原文件
f1 = file('CarTest2-2Answer.txt', 'r')
f2 = file('CarTest2Answer.txt', 'r')

# 临时存贮这两个文件新生成的数据，然后把这些数据写入新的文件carSource.txt中
tmpfile = []
f3 = file('carSource1.txt', 'w')
# 读取文件


def readfile1(fp):
    while True:

        line = fp.readline()
        # 把读取的每一行的字符变成list类型

        if len(line) == 0:
            break
        lineList = line.split()
        # 遇到空白行 则读取文件结束
        # 为了防止lineList的index溢出故，要使用try和except
        try:
            # 把汽车名和value为NULL的行去除
            # 为什么要去除，首先name=NULL，属性和评分没有意义
            # 其次，value = NULL，则name和属性没有意义
            if lineList[3] != 'NULL' and lineList[5] != 'NULL':
                tmpstr = lineList[3] + '         ' + \
                    lineList[4] + '         ' + lineList[5]
                # print tmpstr
                tmpfile.append(tmpstr)
        except:
            print "some"

readfile1(f1)
readfile1(f2)

f3.write('\n'.join(tmpfile))

# 关闭文件
f1.close()
f2.close()
f3.close()
