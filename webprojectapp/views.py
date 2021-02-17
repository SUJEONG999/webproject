from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
from webprojectapp.models import Restaurant  # 상원
from datetime import datetime, timedelta  # 수정
from webprojectapp.models import Hospital  # 강용
from webprojectapp.models import Clinic  # 강용
# from webprojectapp.models import Board  # 하영


# 수정님
def main(request):
    template = loader.get_template('main.html')
    date = datetime.now() - timedelta(1)
    context = {'current_date': date}
    return HttpResponse(template.render(context, request))


def register(request):
    res_data = None
    if request.method == 'POST':
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error'] = '이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username=useremail,
                                            first_name=firstname,
                                            last_name=lastname,
                                            password=password)
            auth.login(request, user)
            redirect("index.html")
    return render(request, 'register.html', res_data)


def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("main")
        else:
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("main")


def only_member(request):
    context = None
    if request.user.is_authenticated:
        context = {'logineduser': request.user.last_name + request.user.first_name}
    return render(request, 'member.html', context)


# 상원
def map1(request):
    search = request.GET.get('search')
    Restaurants = Restaurant.objects.all()
    Rname = []
    Raddress = []
    for rest in Restaurants:
        Rname.append(rest.r_name)
        Raddress.append(rest.r_address)

    if request.method == 'POST':
        txt = (request.POST['text'])
        context = {
            "txt": txt,
            "Rname": Rname,
            "Raddress": Raddress,
            "search": search,
        }
    else:
        context = {
            "Rname": Rname,
            "Raddress": Raddress,
            "search": search,
        }
    return render(request, 'map1.html', context)


# 강용님
def map2(request):
    hospitals = Hospital.objects.all()
    hname = []
    haddress = []
    htype = []
    hnumber = []
    for hospital in hospitals:
        hname.append(hospital.h_name)
        haddress.append(hospital.h_address)
        htype.append(hospital.h_type)
        hnumber.append(hospital.h_number)

    search = request.GET.get('search')
    if request.method == 'POST':
        txt = (request.POST['text'])
        context = {
            "txt": txt,
            "search": search,
            "hospitals": hospitals,
            "hname": hname,
            "haddress": haddress,
            "htype": htype,
            "hnumber": hnumber
        }
    else:
        context = {
            "search": search,
            "hospitals": hospitals,
            "hname": hname,
            "haddress": haddress,
            "htype": htype,
            "hnumber": hnumber
        }
    return render(request, 'map2.html', context)


def map2_1(request):
    clinics = Clinic.objects.all()
    cname = []
    caddress = []
    cnumber = []
    for clinic in clinics:
        cname.append(clinic.name)
        caddress.append(clinic.address)
        cnumber.append(clinic.number)

    search = request.GET.get('search')
    if request.method == 'POST':
        txt = (request.POST['text'])
        context = {
            "txt": txt,
            "search": search,
            "clinics": clinics,
            "cname": cname,
            "caddress": caddress,
            "cnumber": cnumber
        }
    else:
        context = {
            "search": search,
            "clinics": clinics,
            "cname": cname,
            "caddress": caddress,
            "cnumber": cnumber
        }
    return render(request, 'map2_1.html', context)


# 하영님
# def board(request):
#     # 모든 Board를 가져와 boardlist에 저장
#     boardlist = Board.objects.all()
#     context = {'boardlist': boardlist}
#     return render(request, 'board.html', context)
#
#
# def board_view(request, pk):
#     # 게시글(Board) 중 pk를 이용해 하나의 게시글(post)를 검색
#     board = Board.objects.get(pk=pk)
#     return render(request, 'boards/board_view.html', {'board': board})  # 추가
#
#
# def board_write(request):
#     return render(request, 'boards/board_write.html')


# def new_post(request):
#     if request.method == 'POST':
#         if request.POST['mainphoto'] :
#             new_article = Board.objects.create(
#                 no=request.POST['no'],
#                 writer=request.POST['writer'],
#                 postname=request.POST['postname'],
#                 contents=request.POST['contents'],
#                 satisfaction=request.POST['satisfaction'],
#                 mainphoto=request.POST['mainphoto'],
#             )
#         else:
#             new_article = Board.objects.create(
#                 no=request.POST['no'],
#                 writer=request.POST['writer'],
#                 postname=request.POST['postname'],
#                 contents=request.POST['contents'],
#                 satisfaction=request.POST['satisfaction'],
#                 mainphoto=request.POST['mainphoto'],
#             )
#         return redirect('board')
#     return render(request, 'boards/new_write.html')

# def write(request):
#     if request.method == 'POST' and request.user.is_authenticated:
#         writer = request.user
#         postname = request.POST['postname']
#         contents = request.POST['contents']
#         mainphoto = request.POST['mainphoto']
#
#         vdate = Board(
#             writer=request.user,
#             postname=postname,
#             contents=contents,
#             mainphoto=mainphoto)
#         vdate.save()
#         return redirect('board')
#
#
# def remove_board(request, pk):
#     board = Board.objects.get(pk=pk)
#     if request.method == 'POST':
#         board.delete()
#         return redirect('../../')
#     return render(request, 'boards/remove_post.html', {'board': board})