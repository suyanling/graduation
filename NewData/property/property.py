# -*-  coding: utf-8 -*-

# 这个文件作用:
# 1 把小属性变成大属性
# 2 把相同的大属性

# 把一个文件变成一个dict对象


# def fileTodict(fp):
#     dict = {}
#     while True:
# 逐行读取 并把每一行字符串变成list
#         line = fp.readline()
# 读到最后一行 结束
#         if len(line) == 0:
#             break
#         if line not in dict:
#             print line
#             dict[line] = ''
#     return dict


# 把文件变成一个set集合
# def fileToset(file1):
#     lines1 = file1.readlines()
#     lines1 = set(lines1)
#     return lines1

# 把一个文件变成list 晕，晕，晕 测试了dict和set在本程序中只有list合适
def fileTolist(fp):
    lists = []
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fp.readline()
        linelist = line.split()
        linelist = ''.join(linelist)
# 读到最后一行 结束
        if len(line) == 0:
            break
        lists.append(linelist)
    return lists

f1 = file('aftersale.txt', 'r')
list1 = fileTolist(f1)
# set1 = fileToset(f1)

f2 = file('appearance.txt', 'r')
list2 = fileTolist(f2)

f3 = file('comfort.txt', 'r')
list3 = fileTolist(f3)

f4 = file('costperformance.txt', 'r')
list4 = fileTolist(f4)

f5 = file('fuelconsume.txt', 'r')
list5 = fileTolist(f5)

f6 = file('magnification.txt', 'r')
list6 = fileTolist(f6)

f7 = file('power.txt', 'r')
list7 = fileTolist(f7)

f8 = file('room.txt', 'r')
list8 = fileTolist(f8)

f9 = file('safety.txt', 'r')
list9 = fileTolist(f9)

f10 = file('trim.txt', 'r')
list10 = fileTolist(f10)


# 把小属性的值加到大属性身上 之第一步 把小属性变成大属性


def smallTobig(fs, fd):
    tmpList = []
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fs.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        strlist = lineList[1]
        if lineList[1] in list1:
            strlist = "售后"
        elif lineList[1] in list2:
            strlist = "外观"
        elif lineList[1] in list3:
            strlist = "舒适度"
        elif lineList[1] in list4:
            strlist = "性价比"
        elif lineList[1] in list5:
            strlist = "油耗"
        elif lineList[1] in list6:
            strlist = "操控"
        elif lineList[1] in list7:
            strlist = "动力"
        elif lineList[1] in list8:
            strlist = "空间"
        elif lineList[1] in list9:
            strlist = "安全性"
        elif lineList[1] in list10:
            strlist = "内饰"
        # 把没有分类的属性收集起来 放入一个待分属性文件B中
        else:
            readProperty.append(lineList[1])
    # print strlist
        tempstr = lineList[0] + '   ' + strlist + ' ' + lineList[2]
        tmpList.append(tempstr)
    fd.write('\n'.join(tmpList))

# 待分类的属性
readProperty = []

# 把新内容写进NFV_Big.txt文件中
fileS = file('/home/susu/Desktop/NewData/carSource1.txt', 'r')
fileD = file('NFV_Big.txt', 'w')
smallTobig(fileS, fileD)
fileS.close()
fileD.close()

# 待分属性文件B
fb = file('B.txt', 'w')
fb.write('\n'.join(readProperty))


# 任务 把相同的大属性名的value相加


# 把汽车名和大属性通过+连接起来
# 方便下一步 把汽车名共同的属性名相加

# 把这样的形式
# 它   空间 1 转化为
#  它+空间 1这样的格式
def contact(fs, fd):
    listinfo = []
    while True:
                # 逐行读取 并把每一行字符串变成list
        line = fs.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break
        tmp = lineList[0] + '+' + lineList[1] + "        " + lineList[2] + '\n'
        listinfo.append(tmp)

    listinfo.sort()
    fd.write(''.join(listinfo))


fBig = file('NFV_Big.txt', 'r')
fBigContact = file('NFV_Big_contact.txt', 'w')
contact(fBig, fBigContact)
fBig.close()
fBigContact.close()

# 把同一个产品的相同大属性相加


def addBigpp(fs, fd):
    dictinfo = {}
    listinfo = []
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fs.readline()
        lineList = line.split()

        # 读到最后一行 结束
        if len(line) == 0:
            break

        # if dictinfo中没有这个关键字 就把这个关键字和value加入到dictinfo中
        if lineList[0] not in dictinfo and lineList[1] != 'NULL':
            dictinfo[lineList[0]] = int(lineList[1])
        # else 把相应的value做修改
        else:
            try:
                dictinfo[lineList[0]] += int(lineList[1])
            except Exception, e:
                print e
    # sortList = sorted(dictinfo.items(), key=lambda dictinfo: dictinfo[0])
    for (k, v) in dictinfo.items():
        # print v
        tmp = k + " " + str(v) + "\n"
        listinfo.append(tmp)

    listinfo.sort()
    fd.write(''.join(listinfo))

fAddS = file('NFV_Big_contact.txt', 'r')
fAddD = file('NFV_Big_contact_add.txt', 'w')
addBigpp(fAddS, fAddD)

fAddS.close()
fAddD.close()

# 把
# 0.8升车型+内饰 0 这样的形式转化为
# 0.8升车型 内饰 0 这样的形式


def revert(fs, fd):
    listinfo = []
    while True:
        # 逐行读取 并把每一行字符串变成list
        line = fs.readline()
        lineList = line.split()
        # 读到最后一行 结束
        if len(line) == 0:
            break
        line1 = lineList[0].split('+')
        line1 = '   '.join(line1)
        tmp = line1 + '   ' + lineList[1]
        listinfo.append(tmp)

    listinfo.sort()
    fd.write('\n'.join(listinfo))


freS = file('NFV_Big_contact_add.txt', 'r')
fred = file('NFV_Big_1.txt', 'w')
revert(freS, fred)
freS.close()
fred.close()
