from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, JsonResponse, FileResponse
from django.template import loader
#view에 Model(Board 게시글) 가져오기
from .models import Board
#============

# 수정님
def main(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
















# 상원님
def map1(request) :
    template = loader.get_template('map1.html')
    return HttpResponse(template.render(None, request))



















# 강용님
def map2(request) :
    template = loader.get_template('map2.html')
    return HttpResponse(template.render(None, request))



















# 하영

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