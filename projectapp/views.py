from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import  loader
from projectapp.models import Hospital

import random
import datetime



# 수정님
def main(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
















# 상원
def map1(request) :
    template = loader.get_template('map1.html')
    return HttpResponse(template.render(None, request))

















# 강용
def map2(request) :
    hospitals = Hospital.objects.all()

    hname = ['연세대학교강남세브란스병원', '중앙보훈병원', '강동성심병원'];
    haddress = ['서울특별시 강남구 언주로211', '서울특별시 강동구 진황도로 61길 53', '서울특별시 강동구 성안로 150'];
    context = {"hospitals": hospitals, "hname":hname, "haddress":haddress}
    return render(request, 'map2.html', context)


















# 하영님
def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

















