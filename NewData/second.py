#!/usr/bin/python
# -*-  coding: utf-8 -*-

# 对文件进行不同的处理得到相应的文件
# 只取出产品的名字放入name.txt文件中
# 只取出产品的属性放入feature.txt文件中
# 取出产品名,评分值(当产品名和评分都不等于'NULL'的时候)放入nameValue.txt中
f1 = file('carSource1.txt', 'r')

name = file('name.txt', 'w')
feature = file('feature.txt', 'w')
nameValue = file('nameValue.txt', 'w')

nameList = []
featureList = []
nameValueList = []


def readfile2(fp):
    while True:
        line = fp.readline()
        if len(line) == 0:
            break
        lineList = line.split()
        nameList.append(lineList[0])
        tmpstr = lineList[0] + '        ' + lineList[2]
        nameValueList.append(tmpstr)
        if lineList[1] != 'NULL':
            featureList.append(lineList[1])


readfile2(f1)
# 给产品名和属性名去重后 把元素集合类型转化为list类型
nameList = list(set(nameList))
featureList = list(set(featureList))
# 给产品名和属性名排序
nameList.sort()
featureList.sort()
name.write('\n'.join(nameList))
feature.write('\n'.join(featureList))
nameValue.write('\n'.join(nameValueList))

name.close()
feature.close()
nameValue.close()
