# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from Middle.dealdata import*
from Middle.figure import*
from django.http import JsonResponse
import json

# NAMES = ""
# 读取文件的信息


def readfile(fp):
    temp = []
    while True:
        line = fp.readline()
        if len(line) == 0:
            break
        temp.append(line)
    # fp.close()
    return temp


# context是一个dict，key是DOM模板的变量，value是后台填充的数据
def getContext():
    context = {}
    # tmpFile = []
    fproperty = file(
        "/home/susu/Desktop/Middle-Test/Middle/source/property.txt", 'r')
    num = 1
    while True:
        if num > 11:
            break
        # 不使用用大而全的汽车名文件
        # fp = file(
        #     "/home/susu/Desktop/Middle-Test/Middle/source/price" + str(num) + ".txt", 'r')
        # 使用从测试文件里提取出来的文件
        fp = file(
            "/home/susu/Desktop/data/Car/SUM/newP" + str(num) + ".txt", 'r')
        context['price' + str(num)] = readfile(fp)
        num = num + 1
        # tmpFile.append(readfile(fp))

    property = readfile(fproperty)
    # fp.close()

    # context 就是一个dict. name是模板的变量,value就是要替换模板变量的值
    context['property'] = property
    return context
    # return render_to_response('home.html', context)


def home(request):
    print "nameS"
    # NAMES = request.GET.get('nameS', '')
    # singlefigure(NAMES)
    # print NAMES
    # print request.GET.get['nameS', '']
    return form1(request)

# 这是对第一个表单的提交的数据进行处理
# 也就是单产品处理


def form1(request):
    context = getContext()
    names = '汽车名'
    propertys = '属性名'
    value = ''
    # 尝试获取提交的表单中的input的值
    # 可以使用for key in request.GET:或者if 'nameS' in request.GET:
    # 但是不可以直接nameS = req.GET['nameS']
    # tmp = []
    # for key in request.GET:
    #     tmp.append(request.GET[key])
    # context['panelContent'] = ''.join(tmp)
    if 'nameS' in request.GET and 'propertyS' in request.GET:
        names = request.GET['nameS']
        propertys = request.GET['propertyS']
        # if not names and not propertys:
        #     nameProper = namePerperty(names, propertys)
        #     context['panelContent'] = nameProper
        if not names:
            proper = bigProperty(propertys)
            # print "proper", proper
            context['panelContent'] = proper
        elif not propertys:
            value = carName(names)
            context['panelContent'] = value
        else:
            # context['panelContent'] = "抱歉，暂时没有这方面的信息。"
            nameProper = namePerperty(names, propertys)
            context['panelContent'] = nameProper
    context['nameS'] = names
    context['propertyS'] = propertys
    # 某种汽车对应的相应的属性的值
    # figure = allProperty(names)
    # print figure
    # print json.dumps(figure)
    # context['figure'] = json.dumps(figure)
    # JsonResponse(figure)
    return render_to_response('home.html', context)
    # return HttpResponse('home.html', json.dumps(context),
    #                     content_type='application/json')

# 这是对第二个表单提交的数据进行处理
# 也就是多产品处理


def form2(request):
    pass

# 单独请求图表展示产品的属性
# 那么用户的点击两次，进行两次查询。一次是表单提交查询，一次是查看图表显示
# 所以不考虑这个方法

# 不能使用全局变量，因为没有调用函数，所以值没有做任何修改
# print "是否改变"
# print NAMES
# print "*************"


def singlefigure(request):
    print request.get_full_path()
    name = request.GET.get('carname', '')
    dictproperty = allProperty(name)
    print "11111111111111111111111"
    # print dictproperty
    print "singlefigure的参数是否已经传进来了"
    # 使用render_to_response不可以
    # 要使用HttpResponse才可以
    return HttpResponse(json.dumps(dictproperty),
                        content_type='application/json')
