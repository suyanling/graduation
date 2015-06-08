# -*- coding: utf-8 -*-

from recommand import*
from figure import*
# 全局的一个对应的表格
# 1 空间 2 动力 3 操控 4 油耗 5 舒适性 6 外观 7 内饰 8 性价比 9 售后 10 安全性
# value1,value2,value3,value4,value5,value6, value7,value8,value9,value10

# 根据用户选择的汽车的名字 做相应的处理


def carName(na):
    # 测试函数
    # allProperty(na)
    # suggest(na)
    # figureComment(na)
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

# ################################################
# 根据用户选择的汽车的属性 做相应的处理


def lookProperty(proper):
    # file_NPV是汽车名，大属性和value值
    file_NPV = file('/home/susu/Desktop/NewData/total_p.txt', 'r')
    # 把proper的编码unicode变成str
    dict = {}
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = file_NPV.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if not line:
            break
        if lineList[1] == proper and int(lineList[2]) > 1:
            dict[lineList[0]] = int(lineList[2])
    # 给某一个特定的大属性的汽车名和vlaue值组成dict按照dict的value值排序
    # 返回排序的结果
    dict = sorted(dict.iteritems(), key=lambda d: d[1], reverse=True)
    file_NPV.close()
    return dict


# bigProperty的作用
# 用户只是选择属性时，推荐该属性比较好的汽车的类型
# 用户选择汽车名和属性时，推荐比该汽车的属性更好的汽车类型


def bigProperty(proper, na):
    proper = proper.encode('utf-8')
    result = ''
    # propertyInterval(proper)
    dict = lookProperty(proper)
    # str1是存储非常好的车型（也就是value大于2的车型）
    # str 是存贮比较好的车型（也就是大于1的车型）
    # str3,str4相当于str1和str2
    # str1和str2是用户只是选择属性时起作用
    # str3和str4是用户同时选择属性和名字
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    for key, val in dict:
        if val > 2:
            str1 += key + "  "
        else:
            str2 += key + "  "
    if not dict:
        result = "暂时没有《" + proper + "》这方面比较好的车型"
    else:
        if na == "":
            result = "《" + proper + "》这方面"
            if str1 != "":
                str1 = "非常好的车型是：" + str1 + ","
            if str2 != "":
                str2 = "比较好的车型是:" + str2+'\n'
            result = str1 + str2
            return result
        else:
            # allProperty(na)返回na的所有的属性和对应的value值
            dictproperty = allProperty(na)
            # pvalue = proper对应的value值
            pvalue = 0
            for k, v in dictproperty.items():
                if k == proper:
                    pvalue = v
            na = na.encode('utf-8')
            # print "pvalue-----------------------------"
            # print pvalue
            # print "pvalue-----------------------------"
            for key, val in dict:
                if key != na and val >= pvalue:
                    if val > 2:
                        str3 += key + "  "
                    else:
                        str4 += key + "  "
            if str3 != "":
                str3 = "比"+na+"的"+proper+"好很多的车型是：" + str3 + ","
            if str4 != "":
                str4 = "比"+na+"的"+proper+"好一些或者相当的车型是：" + str4 + ","
            result = str3 + str4
            return result

# 根据属性给推荐的汽车，把该汽车所在的价格区间展示出来


def propertyInterval(proper):
    proper = proper.encode('utf-8')
    # 文件w_P1和相应的价格区间对应表
    dictRespon = {
        1: "5w以下",
        2: "5w-10w",
        3: "10w-15w",
        4: "15w-20w",
        5: "20w-25w",
        6: "25w-30w",
        7: "30w-35w",
        8: "35w-50",
        9: "50w-70w",
        10: "70w-100w",
        11: "100w及以上"
    }
    dict = lookProperty(proper)

    # dict_interval的key是汽车名，value是对应的汽车所在的价格区间
    dict_interval = {}
    # strResult存贮返回的值
    strResult = ""
    for key, val in dict:
        num = 1
        while True:
            if num > 11:
                break
            # 使用从测试文件里提取出来的文件
            fp = file(
                "/home/susu/Desktop/NewData/crawler/w_P" + str(num) + ".txt", 'r')
            #     dict_interval[key] = num
            while True:
                line = fp.readline()
                # 去除每一行的空格
                line = line.split()
                line = ''.join(line)
                # 读到最后一行 结束
                if len(line) == 0:
                    break
                if key == line:
                    dict_interval[key] = num
            fp.close()
            num = num + 1
        # tmpFile.append(readfile(fp))
    # dictstr是每个价格区间的评论
    dictstr = {}
    # 初始化dictstr
    for x in range(1, 12):
        dictstr[x] = ""
    # print dictstr
    # print dict_interval
    for k, v in dict_interval.items():
        for x in range(1, 12):
            if x == v:
                dictstr[x] += k + "     "
    # print dictstr
    for k, v in dictstr.items():
        if v != "":
            strResult += dictRespon[k] + ": " + v + "； "
    # print "最终结果"
    # print strResult
    return strResult

# ################################################

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

# 推荐同一个价位相同的其他汽车的相应的评论


def suggest(na):
    # print "11111111111111111"
    str = '推荐：同一个价位，跟它相当或比它好的汽车有:'
    nameslist = recommand(na)
    # print nameslist
    # if not nameslist:
    #     str = '同一个价位比较好的汽车有:'
    for k in nameslist:
        str += k + "    "
    # print str
    return str


# 给汽车的各个大属性做相应的评论
def figureComment(na):
    # strsum 是返回的评论
    # str1_1是str1 一开始的一个备份
    strsum = ''
    str1 = "非常好的属性："
    str1_1 = "非常好的属性："

    str2 = "比较好的属性："
    str2_1 = "比较好的属性："

    str3 = "一般的属性："
    str3_1 = "一般的属性："

    str4 = "不好的属性："
    str4_1 = "不好的属性："

    str5 = "非常不好的属性："
    str5_1 = "非常不好的属性："
    dictfigure = allProperty(na)
    for k, v in dictfigure.items():
        # print k, v
        if v == 0:
            str3 += k + "  "
        elif v > 2:
            str1 += k + "   "
        elif v > 0:
            str2 += k + "   "
        elif v < -2:
            str5 += k + "   "
        elif v < 0:
            str4 += k + "   "
    # print str1, str2, str3, str4, str5
    if str1 != str1_1:
        strsum += str1 + "。"
    if str2 != str2_1:
        strsum += str2 + "。"
    if str4 != str4_1:
        strsum += str4 + "。"
    if str5 != str5_1:
        strsum += str5 + "。"
    if str3 != str3_1:
        strsum += str3 + "。"
    # print "12345667"
    # print strsum
    return strsum
