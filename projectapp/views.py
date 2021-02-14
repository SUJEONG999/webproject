from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import  loader
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Restaurant # 상원
from datetime import datetime, timedelta # 수정
from projectapp.models import Hospital # 강용
from projectapp.models import Clinic # 강용




# 수정님
def main(request) :
    template = loader.get_template('index.html')
    date = datetime.now() - timedelta(1)
    context = { 'current_date' : date }
    return HttpResponse(template.render(context, request))
def register(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password',None)
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username = useremail,
                            first_name = firstname,
                            last_name = lastname,
                            password = password)
            auth.login(request, user)
            redirect("index.html")
    return render(request, 'register.html', res_data)
def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("main")
        else :
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'login.html')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("main")
def only_member(request) :
    context = None
    if request.user.is_authenticated:
        context = {'logineduser': request.user.last_name+request.user.first_name}
    return render(request, 'member.html', context)


# 상원
def map1(request) :
    search = request.GET.get('search')
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
            "Raddress":Raddress,
            "search":search,
        }
    else :
        context = {
            "Rname":Rname,
            "Raddress":Raddress,
            "search":search,
        }
    return render(request, 'map1.html', context)



# 강용님
def map2(request) :
    hospitals = Hospital.objects.all()
    hname = []
    haddress = []
    for hospital in hospitals:
        hname.append(hospital.h_name)
        haddress.append(hospital.h_address)
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

def board_view(request) :
    boards = board_list.objects.all()
    return render(request, 'boards/board_view.html', {'boards':boards})

def board_write(request) :
    return render(request, 'boards/board_write.html')

def board_edit(request) :
    return render(request, 'boards/board_edit.html')

def board_list(request):
    #모든 Board 내용을 가져와 boardlist에 저장
    boardlist = Board.objects.all().order_by('-id') #최신사항부터
    #board_list를 열 때, 모든 Board인 boardlist을 가져오겠다
    return render(request, 'boards/board_list.html', {'boardlist':boardlist})

def new(request):
    return render(request, 'new.html')

def post(request):
    if request.method == 'POST':
        post = Board()
        post.store = request.POST['store'],
        post.date = request.POST['date'],
        post.customers = request.POST['customers'],
        post.satisfaction = request.POST['satisfaction'],
        post.title = request.POST['title'],
        post.content = request.POST['content'],
        post.imagefile=  request.POST['imagefile'],
        board.pub_date = timezone.datetime.now(),
        board.save()
        return redirect('/board/' + str(board.id))
