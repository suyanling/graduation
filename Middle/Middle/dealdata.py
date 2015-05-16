# -*- coding: utf-8 -*-

from recommand import*
from figure import*
# 全局的一个对应的表格
# 1 空间 2 动力 3 操控 4 油耗 5 舒适性 6 外观 7 内饰 8 性价比 9 售后 10 安全性
# value1,value2,value3,value4,value5,value6, value7,value8,value9,value10

# 根据用户选择的汽车的名字 做相应的处理


def carName(na):
    # 根据函数
    allProperty(na)
    suggest(na)

    # file_NV是汽车名和value值
    file_NV = file('/home/susu/Desktop/NewData/total.txt', 'r')
    # print "传入的参数是1:", na, "有没有空格啊"
    # 把na的编码unicode变成str
    na = na.encode('utf-8')
    value = ''
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = file_NV.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if not line:
            break
        # print type(lineList[0])
        # str
        # print type(na)
        # unicode
        # strlist = unicode(lineList[0])
        # print type(strlist)
        if lineList[0] == na:
            value = lineList[1]

    file_NV.close()
    return score(na, '', value)

# 测试文件和home.py文件里面调用的carName传的参数不是同类型的
# 一个是str类型一个是unicode类型 故如果两个文件同时调用这函数
# 就会出现编码的错误
# value = carName('奇瑞QQ')
# print value

# 当返回的value=''会发生这样的错误
# invalid literal for int() with base 10: ''


# 根据用户选择的汽车的属性 做相应的处理


def bigProperty(proper):
    # file_NPV是汽车名，大属性和value值
    file_NPV = file('/home/susu/Desktop/NewData/total_p.txt', 'r')
    # 把proper的编码unicode变成str
    proper = proper.encode('utf-8')
    dict = {}
    result = ''
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = file_NPV.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if not line:
            break
        if lineList[1] == proper and int(lineList[2]) > 0:
            dict[lineList[0]] = lineList[2]
    # 给某一个特定的大属性的汽车名和vlaue值组成dict按照dict的value值排序
    # 返回排序的结果
    dict = sorted(dict.iteritems(), key=lambda d: d[1], reverse=True)
    if not dict:
        result = "暂时没有《" + proper + "》这方面比较好的车型"
    else:
        result = "《" + proper + "》这方面比较好的车型是：" + "\n"
        for key, val in dict:
            result += key + '\n\n'
    file_NPV.close()
    return result


# 根据用户选择的汽车名和属性名 做相应的处理
def namePerperty(na, proper):
    # file_NPV是汽车名，大属性和value值
    file_NPV = file('/home/susu/Desktop/NewData/total_p.txt', 'r')
    # 把na的编码unicode变成str
    proper = proper.encode('utf-8')
    na = na.encode('utf-8')
    value = ''
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = file_NPV.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if not line:
            break
        if lineList[0] == na:
            value = lineList[2]
    file_NPV.close()
    return score(na, proper, value)


# 根据汽车对应的分值返回该汽车的评论

def score(name, proper, val):
    if val == '':
        val = '0'
    val = int(val)
    str = ''
    sum = ''
    if proper == '':
        sum = "总体"
    if val >= 3:
        str = name + sum + "与其他汽车相比，" + proper + "非常好！！！"
    elif val <= -3:
        str = name + sum + "与其他汽车相比，" + proper + "非常差！！！"
    elif val == 2:
        str = name + sum + "与其他汽车相比，" + proper + "比较好！！"
    elif val == 1:
        str = name + sum + "与其他汽车相比，" + proper + "挺好的！"
    elif val == 0:
        str = name + sum + "与其他汽车相比，" + proper + "一般。"
    elif val == -1:
        str = name + sum + "与其他汽车相比，" + proper + "不是很好！"
    elif val == -2:
        str = name + sum + "与其他汽车相比，" + proper + "比较不好！！"
    return str

# print score(value)


def suggest(na):
    # print "11111111111111111"
    str = '同一个价位比较好的汽车有:'
    nameslist = recommand(na)
    print nameslist
    # if not nameslist:
    #     str = '同一个价位比较好的汽车有:'
    for k in nameslist:
        str += k + "    "
    print str
    return str
