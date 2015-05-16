# -*- coding: utf-8 -*-
import urllib
import re

# 捉取不同价格区间的汽车的名字 然后把她们放在不同的文件中
# 为了方便后面的操作，把文件名进行修改
# f1 = file("5w.txt", 'w')
# f2 = file("5_10w.txt", 'w')
# f3 = file("10_15w.txt", 'w')
# f4 = file("15_20w.txt", 'w')
# f5 = file("20_25w.txt", 'w')
# f6 = file("25_30w.txt", 'w')
# f7 = file("30_35w.txt", 'w')
# f8 = file("35_50w.txt", 'w')
# f9 = file("50_70w.txt", 'w')
# f10 = file("70_100w.txt", 'w')
# f11 = file("100w.txt", 'w')
f1 = file("w1.txt", 'w')
f2 = file("w2.txt", 'w')
f3 = file("w3.txt", 'w')
f4 = file("w4.txt", 'w')
f5 = file("w5.txt", 'w')
f6 = file("w6.txt", 'w')
f7 = file("w7.txt", 'w')
f8 = file("w8.txt", 'w')
f9 = file("w9.txt", 'w')
f10 = file("w10.txt", 'w')
f11 = file("w11.txt", 'w')

# 捉取页面的html代码


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 活取页面的某个特定的元素 使用正则表达式
# 并把这些匹配的元素写入文件中


def getElements(html, f):

    # 把gb2313编码变成unicode编码
    # ignore忽视非法字符
    html = html.decode('gb2312', 'ignore')

    # 使用正则 匹配这样的字符(>北汽威旺205</a></h4>)
    elements = re.compile(u">.{1,20}</a>\s?</h4>")
    eleList = re.findall(elements, html)
    # f.write(''.join(eleList).encode('utf-8'))
    tmpstr = ''.join(eleList).encode('utf-8')
    # 给获取的元素做处理 去除无用的符号</a></h4>
    delSymbol = tmpstr.split("</a></h4>")
    delSymbol_1 = '\n'.join(delSymbol)
    # print delSymb
    # 给获取的元素做处理 去除无用的符号>
    delSymbol_1 = delSymbol_1.split(">")
    delSymbol_2 = ''.join(delSymbol_1)
    f.write(delSymbol_2)
    # print eleList
    f.close()

# 5w以下的汽车
html1 = getHtml("http://www.autohome.com.cn/car/1_5-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html1, f1)

# 5w-10w的汽车
html2 = getHtml("http://www.autohome.com.cn/car/5_10-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html2, f2)

# 10w-15w的汽车
html3 = getHtml(
    "http://www.autohome.com.cn/car/10_15-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html3, f3)

# 15w-20w的汽车
html4 = getHtml(
    "http://www.autohome.com.cn/car/15_20-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html4, f4)

# 20w-25w的汽车
html5 = getHtml(
    "http://www.autohome.com.cn/car/20_25-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html5, f5)

# 25w-30w的汽车
html6 = getHtml(
    "http://www.autohome.com.cn/car/25_30-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html6, f6)

# 30w-35w的汽车
html7 = getHtml(
    "http://www.autohome.com.cn/car/30_35-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html7, f7)

# 35w-50w的汽车
html8 = getHtml(
    "http://www.autohome.com.cn/car/35_50-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html8, f8)

# 50w-70w的汽车
html9 = getHtml(
    "http://www.autohome.com.cn/car/50_70-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html9, f9)

# 70w-100w的汽车
html10 = getHtml(
    "http://www.autohome.com.cn/car/70_100-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html10, f10)

# 100w以上的汽车
html11 = getHtml(
    "http://www.autohome.com.cn/car/100_100-0.0_0.0-0-0-0-0-0-0-0-0/")
getElements(html11, f11)
