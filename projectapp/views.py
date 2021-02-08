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
    template = loader.get_template('map2.html')
    return HttpResponse(template.render(None, request))

















# 하영님
def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

















