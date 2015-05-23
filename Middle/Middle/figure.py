# -*- coding: utf-8 -*-

# 获取汽车的所有的属性 可以用于制作图表的数据


def allProperty(na):
    file_NPV = file('/home/susu/Desktop/NewData/total_p.txt', 'r')
    # print "typpeof na"
    # print type(na)
    na = na.encode('utf-8')
    # print type(na)
    # 下面的value的值对应的大属性
    # 大属性的顺序为:
    # 1 空间 2 动力 3 操控 4 油耗 5 舒适性 6 外观 7 内饰 8 性价比 9 售后 10 安全性
    value1 = 0
    value2 = 0
    value3 = 0
    value4 = 0
    value5 = 0
    value6 = 0
    value7 = 0
    value8 = 0
    value9 = 0
    value10 = 0

    # 存贮大属性的名字和相应的value值
    dictproperty = {}
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = file_NPV.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if not line:
            break
        if lineList[0] == na:
            if lineList[1] == '空间':
                value1 = int(lineList[2])
            elif lineList[1] == '动力':
                value2 = int(lineList[2])
            elif lineList[1] == '操控':
                value3 = int(lineList[2])
            elif lineList[1] == '油耗':
                value4 = int(lineList[2])
            elif lineList[1] == '舒适性':
                value5 = int(lineList[2])
            elif lineList[1] == '外观':
                value6 = int(lineList[2])
            elif lineList[1] == '内饰':
                value7 = int(lineList[2])
            elif lineList[1] == '性价比':
                value8 = int(lineList[2])
            elif lineList[1] == '售后':
                value9 = int(lineList[2])
            elif lineList[1] == '安全性':
                value10 = int(lineList[2])
    # for x in xrange(0, 11):
    #     print "value"+str(x)
    # print value1, value2, value3, value4, value5, value6, value7, value8,
    # value9, value10
    file_NPV.close()
    dictproperty['空间'] = value1
    dictproperty['动力'] = value2
    dictproperty['操控'] = value3
    dictproperty['油耗'] = value4
    dictproperty['舒适性'] = value5
    dictproperty['外观'] = value6
    dictproperty['内饰'] = value7
    dictproperty['性价比'] = value8
    dictproperty['售后'] = value9
    dictproperty['安全性'] = value10
    # print dictproperty
    # for k, v in dictproperty.items():
    #     print k, v
    return dictproperty
