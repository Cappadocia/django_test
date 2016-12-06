#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from web_test.models import Asset
# Create your views here.

def index(request):
    
    return HttpResponse('index')

def login(request):
    
    return HttpResponse('login')


def list(request,id,name):
    print(id,name)    
    return HttpResponse('list')


def Add(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse('OK')

def Delete(request,id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('OK')
    
def Update(request,id,hostname):
    #方法一
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()
    #方法2,批量修改
    #Asset.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('OK') 

def GET(request,hostname):

    '''
    assetlist = Asset.objects.filter(hostname__contains=hostname)
    for item in assetlist:
        print(item.id)
    print(assetlist)
    return HttpResponse('OK')   
    '''
    alldata = Asset.objects.all().values('id')
    print(alldata)
    print(alldata.query)
    temp = Asset.objects.all()[0:2]
    print(temp)
    
    return HttpResponse('OK')


def AssetList(request):
    asset_list = Asset.objects.all()
    #把数据嵌套到HTML中
    #把字符串放回给用户
    result = render_to_response('assetlist.html',{'data':asset_list,'user':11479})
    return 
    