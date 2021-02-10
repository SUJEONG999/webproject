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
















# 상원님
def map1(request) :
    template = loader.get_template('map1.html')
    return HttpResponse(template.render(None, request))



















# 강용님
def map2(request) :
    template = loader.get_template('map2.html')
    return HttpResponse(template.render(None, request))



















# 하영(2/5)
from django.shortcuts import render

def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

def board_view(request) :
    return render(request, 'boards/board_view.html')

def board_write(request) :
    return render(request, 'boards/board_write.html')

def board_edit(request) :
    return render(request, 'boards/board_edit.html')

def board_list(request):
    return render(request, 'boards/board_list.html')

#submit 연결 함수
def new(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                store=request.POST['store'],
                date=request.POST['date'],
                customers=request.POST['customers'],
                satisfaction=request.POST['satisfaction'],
                title=request.POST['title'],
                content=request.POST['content'],
                imagefile=request.POST['imagefile'],
            )
        else:
            new_article=Post.objects.create(
                store=request.POST['store'],
                date=request.POST['date'],
                customers=request.POST['customers'],
                satisfaction=request.POST['satisfaction'],
                title=request.POST['title'],
                content=request.POST['content'],
                imagefile=request.POST['imagefile'],
            )
        return redirect('/board/')
    return render(request, 'boards/board_write.html')

# =======


# 페이징 처리 / 글 리스트 보기
#
# from django.views.generic import ListView
# from .models import Board
#
# class BoardListView(ListView):
#     model = Board
#     paginate_by = 10
#     template_name = 'board/board_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
#     context_object_name = 'board_list'        #DEFAULT : <model_name>_list
#
#     def get_queryset(self):
#         board_list = Board.objects.order_by('-id')
#         return board_list
#
# # 페이징 처리 / 페이지네이션 커스텀
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     paginator = context['paginator']
#     page_numbers_range = 5
#     max_index = len(paginator.page_range)
#
#     page = self.request.GET.get('page')
#     current_page = int(page) if page else 1
#
#     start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#     end_index = start_index + page_numbers_range
#     if end_index >= max_index:
#         end_index = max_index
#
#     page_range = paginator.page_range[start_index:end_index]
#     context['page_range'] = page_range
#
#     return context

# 게시글 검색기능 구현
# from django.contrib import messages
# from django.db.models import Q
#
#
# def get_queryset(self):
#     search_keyword = self.request.GET.get('q', '')
#     search_type = self.request.GET.get('type', '')
#     notice_list = Board.objects.order_by('-id')
#
#     if search_keyword:
#         if len(search_keyword) > 1:
#             if search_type == 'all':
#                 search_board_list = board_list.filter(
#                     Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
#                         writer__user_id__icontains=search_keyword))
#             elif search_type == 'title_content':
#                 search_board_list = board_list.filter(
#                     Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
#             elif search_type == 'title':
#                 search_board_list = board_list.filter(title__icontains=search_keyword)
#             elif search_type == 'content':
#                 search_board_list = board_list.filter(content__icontains=search_keyword)
#             elif search_type == 'writer':
#                 search_board_list = board_list.filter(writer__user_id__icontains=search_keyword)
#
#             return search_board_list
#         else:
#             messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
#     return board_list
#
# def get_context_data(self, **kwargs):
#     search_keyword = self.request.GET.get('q', '')
#     search_type = self.request.GET.get('type', '')
#
#     if len(search_keyword) > 1 :
#         context['q'] = search_keyword
#     context['type'] = search_type
#
#     return context

#게시글 검색기능 구현2
# from django import forms
#
# class PostSearchForm(forms.Form):
#     search_word = forms.CharField(label='Search Word')
#
# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name = 'blog/post_search.html'
#
#     def form_valid(self, form):
#         searchWord = form.cleaned_data['search_word']
#         post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
#
#         context = {}
#         context['form'] = form
#         context['search_term'] = searchWord
#         context['object_list'] = post_list
#
#         return render(self.request, self.template_name, context)
#
# import os
# from django.http import HttpResponse, Http404
# import mimetypes
#
#
# def notice_download_view(request, pk):
#     notice = get_object_or_404(Notice, pk=pk)
#     url = notice.upload_files.url[1:]
#     file_url = urllib.parse.unquote(url)
#
#     if os.path.exists(file_url):
#         with open(file_url, 'rb') as fh:
#             quote_file_url = urllib.parse.quote(notice.filename.encode('utf-8'))
#             response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
#             response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
#             return response
#         raise Http404
