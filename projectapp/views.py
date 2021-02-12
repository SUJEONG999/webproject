from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import  loader
from .models import Restaurant
import random
import datetime



# 수정님
def main(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
















# 상원
def map1(request) :
    Restaurants = Restaurant.objects.all()
    Rname = []
    Raddress = []
    for rest in Restaurants :
        Rname.append(rest.r_name)
        Raddress.append(rest.r_address)

    if request.method == 'POST':
        txt = (request.POST['text'])
        context = {
            "txt":txt,
            "Rname":Rname,
            "Raddress":Raddress
        }
    else :
        context = {
            "Rname":Rname,
            "Raddress":Raddress
        }
    return render(request, 'map1.html', context)








# 강용님
def map2(request) :

    return render(request, 'map2.html')
















# 하영님
def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))
















