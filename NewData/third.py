#!/usr/bin/python
# -*-  coding: utf-8 -*-

# 把相同的名字的value值相加，算出每一种汽车的总的评分
# 从使用list结构来操作改为dict结构来
f1 = file('carSource1.txt', 'r')
f2 = file('addNameValue', 'w')
dict = {}
list = []


def addNV(fp):
    while True:
        line = fp.readline()
        if len(line) == 0:
            break
        lineList = line.split()
        if lineList[0] not in dict:
            print lineList[0], lineList[2]
            try:
                dict[lineList[0]] = int(lineList[2])
            except Exception, e:
                print e
        else:
            try:
                dict[lineList[0]] += int(lineList[2])
            except Exception, e:
                print e

addNV(f1)
for (k, v) in dict.items():
    tmp = k + "         " + str(v) + "\n"
    list.append(tmp)

list.sort()
f2.write(''.join(list))
f1.close()
f2.close()
