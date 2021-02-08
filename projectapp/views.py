from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import  loader
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
    lat = [37.5115, 37.5094, 37.5080, 37.5110, 37.5088]
    lng = [127.0500, 127.0503, 127.0600, 127.0590, 127.0560];
    hname = ['병원1', '병원2', '병원3', '병원4', '병원5'];
    address = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'];
    context = {
        'lat': lat, 'lng': lng, 'hname': hname, 'address': address
    }

    return render(request, 'map2.html', context)



















# 하영님
def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

















