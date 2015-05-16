# -*- coding: utf-8 -*-

tmp = 1
while True:
    if tmp > 11:
        break
    fp = file(
        "/home/susu/Desktop/Middle-Test/Middle/source/price" + str(tmp) + ".txt", 'r')
    tmp = tmp + 1
    print fp
