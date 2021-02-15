from django.shortcuts import render, redirect
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
    # 모든 Board를 가져와 boardlist에 저장
    boardlist = Board.objects.all()
    context = {'boardlist':boardlist}
    return render(request, 'board.html', context)

def board_view(request, pk) :
    # 게시글(Board) 중 pk를 이용해 하나의 게시글(post)를 검색
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/board_view.html', {'board':board}) #추가

def board_write(request) :
    return render(request, 'boards/board_write.html')

def write(request):
    if request.method == 'POST' and request.user.is_authenticated:
        writer = request.user
        postname = request.POST['postname']
        contents = request.POST['contents']
        mainphoto = request.POST['mainphoto']

        vdate = Board(
        writer=request.user,
        postname=postname,
        contents=contents,
        mainphoto=mainphoto)
        vdate.save()
        return redirect('board')

def remove_board(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('../../')
    return render(request, 'boards/remove_post.html', {'board': board})

@property
def click(self):
    self.hits += 1
    self.save()