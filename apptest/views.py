from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
# from . import models
# import apptest.models as models
from . import models

# Create your views here.
def index(request):
    pagetitle = "ORM哈哈哈哈"
    argofloats = models.Argometa.objects.filter(datacentre='HZ')
    # argofloats = argofloats[0:10]8
    response = render(request, template_name='apptest/index.html',context=locals())
    response['Access-Control-Allow-Origin'] = "*"
    response['Access-Control-Allow-Headers'] = "*"
    response['Access-Control-Expose-Headers'] = "*"
    response['Access-Control-Allow-Methods'] = "*"
    response['Access-Control-Allow-Credentials'] = "true"
    # 允许X-frame
    response['X-Frame-Options'] = 'ALLOWALL'
    return response


def test01(request):
    # 测试HttpResponse,返回普通文本
    result = "你相信光吗？"
    return HttpResponse(result)

def test02(request):
    # 测试JsonResponse,返回Json
    result = {"poet":"xx中文"}
    json_dumps_params = {'ensure_ascii': False}
    return JsonResponse(result, json_dumps_params=json_dumps_params)

# 获取浮标路径
def testargopath(request, platformname):
    # 5906039/6902847
    # ajax
    records = models.Targoheader.objects.values('cyclenumber', 'longitude', 'latitude')
    # print(str(records.query))
    records = records.filter(platformname=platformname)
    records = records.order_by('cyclenumber')
    # QuerySet
    # select 'cyclenumber', 'longitude', 'latitude' from table where pid = pid order by cyclenumber
    data = {}
    data['result'] = list(records.values('cyclenumber', 'longitude', 'latitude'))
    return JsonResponse(data)

# 获取温盐数据
def getTemAndSalt(request,platformnumber,cyclenumber):
    temp = []
    salt = []
    records = models.Argocore.objects.only(
        'cpressure', 'ctemperature', 'csalinity')
    # platformnumber=2900322, cyclenumber=1
    records = records.filter(
        platformnumber=platformnumber, cyclenumber=cyclenumber)
    records = records.order_by('cpressure')
    for record in records:
        temp.append([float(record.ctemperature),
                     float(record.cpressure)])
        salt.append([float(record.csalinity),
                     float(record.cpressure)])
    return JsonResponse({'temp':temp, 'salt': salt})

