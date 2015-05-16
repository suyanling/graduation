# -*- coding: utf-8 -*-
#
# 下面是通过set作用过后的
# 各种集合的操作
# 集合的并 collect1 | collect2
# 集合的交 collect1 & collect2
# 集合的差 collect1 -  collect2 (在collect1中,但不在collect2中)
# 集合的对差 collect1 ^ collect2 (在collect1或者但不在collect2中,但不会同时出现在二者中)

# 返回两个元素集合


def collections(file1, file2):

    # 读取文件的内容
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    # 把内容变成元素集合 方便下面的元素集合运算
    lines1 = set(lines1)
    lines2 = set(lines2)
    return lines1, lines2

# 两个集合的并


def union(colle1, colle2):
    uni = colle1 | colle2
    return uni

# 两个集合的交


def intersect(colle1, colle2):
    intersect = colle1 & colle2
    return intersect


# 两个集合的差
def difference(colle1, colle2):
    diff = colle1 - colle2
    return diff

# 两个集合的对差


def symmetric_difference(colle1, colle2):
    sdiff = colle1 ^ colle2
    return sdiff


# 把集合元素通过list转换成string
def setStr(set):
    tmp = []
    for key in set:
        tmp.append(key)
    # print ''.join(tmp)
    # tmp 排序
    tmp.sort()
    return ''.join(tmp)
