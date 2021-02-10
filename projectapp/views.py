from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import  loader
from projectapp.models import Hospital
from projectapp.models import Clinic

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
    hname = []
    haddress = []
    for hospital in hospitals:
        hname.append(hospital.name)
        haddress.append(hospital.address)
    context = {"hospitals":hospitals, "hname":hname, "haddress":haddress}
    return render(request, 'map2.html', context)

def map2_1(request) :
    clinics = Clinic.objects.all()
    cname = []
    caddress = []
    for clinic in clinics:
        cname.append(clinic.name)
        caddress.append(clinic.address)
    context = {"clinics":clinics, "cname":cname, "caddress":caddress}
    return render(request, 'map2_1.html', context)


















# 하영님
def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

















