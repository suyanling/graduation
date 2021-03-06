# -*- coding: utf-8 -*-
# 把测试文件name.txt和A1.txt文件进行相交
# 得到相应的文件
from setCollect import *

fname = file('/home/susu/Desktop/NewData/name.txt', 'r')
fa = file('/home/susu/Desktop/NewData/crawler/A1.txt', 'r')
fdiff = file('diffName.txt', 'w')
finters = file('intersectName.txt', 'w')

colle1, colle2 = collections(fname, fa)
# colle1,colle2两个集合的交集
inters = intersect(colle1, colle2)
# 在集合colle2中但不在colle1
diff = difference(colle2, colle1)
finters.write(setStr(inters))
fdiff.write(setStr(diff))

fname.close()
fa.close()
fdiff.close()
finters.close()
