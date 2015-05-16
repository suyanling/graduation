# -*- coding: utf-8 -*-
# 爬取新浪网上所有的汽车名
# 这个大而且全的汽车名是否要和原来的大而且全的汽车名进行
# 合并 去重 不停的校对
import urllib
import re

f1 = file("car.txt", 'w')


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getElements(html, f):

    # 使用正则 匹配这样的字符
    # <a href="#" onclick="go_url(87, 2,'m5'); return false;" title="奥德赛">
    elements = re.compile(u"title=.{1,30}>")
    eleList = re.findall(elements, html)
    for key in eleList:
        print key
    tmpstr = ''.join(eleList)
    # eleList1 = tmpstr.split()

    # 给获取的元素做处理 去除无用的符号</a></h4>
    delSymbol = tmpstr.split("title=\"")
    delSymbol_1 = ''.join(delSymbol)
    # 给获取的元素做处理 去除无用的符号>
    delSymbol_1 = delSymbol_1.split("\">")
    delSymbol_2 = '\n'.join(delSymbol_1)
    f.write(delSymbol_2)
    # f.write(tmpstr)
    # print eleList
    f.close()

html1 = getHtml(
    "car.html")
# print html1
getElements(html1, f1)
