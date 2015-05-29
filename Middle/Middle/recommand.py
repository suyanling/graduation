# -*- coding: utf-8 -*-

# 给汽车所在的价格区间相应的value值排序,推荐前三名比较好的汽车
# 找到用户选择的汽车名所在的价格区间,
# 因为一个汽车名,可能在多个价格区间,
# 故,需要把相应的价格区间文件的路径存储起来


def price(na):
    # 传进来的字符的编码是unicode,要转化为字符编码
    # print type(na)
    # na = na.encode('utf-8')
    # 存放汽车名所在的价格区间文件的路径
    tmppath = []
    num = 1
    while True:
        if num > 11:
            break
        fileS = file(
            "/home/susu/Desktop/NewData/crawler/" + "w_PV" + str(num) + ".txt", 'r')
        tmpstr = "/home/susu/Desktop/NewData/crawler/" + \
            "w_PV" + str(num) + ".txt"
        while True:
            # 逐行读取 并把每一行字符串变成list
            line = fileS.readline()
            lineList = line.split()
            # 读到最后一行 结束
            if len(line) == 0:
                break
            # 找出na所在的价格区间文件
            try:
                if lineList[0] == na:
                    tmppath.append(tmpstr)
            except Exception, e:
                print e
        num = num + 1
    return tmppath

# 对返回的价格区间里面的内容做相应的排序


def recommand(na):
    # 之所以要传进参数na,是因为要把na排除
    # 你要推荐其他的汽车产品,肯定不可能还要把自己也算进
    # 传进来的字符的编码是unicode,要转化为字符编码
    na = na.encode('utf-8')
    # 存放name 跟 value
    dict = {}
    # navalue 原来汽车对应的value
    # 跟原来的汽车差不多，或者是比原来的汽车更好才推荐
    # 而且，推荐前5个，也就是最好的5个
    navalue = 0
    tmppath = price(na)
    for path in tmppath:
        files = file(path, 'r')
        while True:
            # 逐行读取 并把每一行字符串变成list
            line = files.readline()
            lineList = line.split()

            # 读到最后一行 结束
            if len(line) == 0:
                break
            if lineList[0] not in dict and lineList[0] != na:
                dict[lineList[0]] = int(lineList[1])
            if lineList[0] == na:
                navalue = int(lineList[1])
    # 给dict根据value值排序,前五的汽车
    dict1 = sorted(dict.iteritems(), key=lambda d: d[1], reverse=True)
    # print "OH MY GOD"
    # print navalue
    # print "OH MY GOD"
    tmpname = []
    num = 1
    for k, v in dict1:
        if num > 5:
            break
        if v > 1 and v >= navalue:
            tmpname.append(k)
        num = num + 1
    return tmpname
    # print tmpname
    # for key in tmpname:
    #     print key
