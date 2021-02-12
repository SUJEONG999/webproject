# 하영
from uuid import uuid4
from datetime import datetime
from django.db import models

class Board(models.Model):
    writer = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    store = models.CharField(max_length=30, verbose_name='방문매장')
    visited_date = models.DateTimeField(verbose_name='방문일자')
    customers = models.CharField(max_length=30, default="가족", verbose_name='동반고객')
    satisfaction = models.PositiveIntegerField(default=5, verbose_name='만족도')
    title = models.CharField(max_length=128, default="제목", verbose_name='제목')
    content = models.TextField(default="내용", verbose_name='내용')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    stars = models.PositiveIntegerField(default=0, verbose_name='추천수')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='작성 시간')
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='수정 시간')
    upload_files = models.ImageField(blank=True, null=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')

#관리자 페이지에서 정상적으로 title 테이블 출력
    def __str__(self):
        return self.title


@property
def click(self):
    self.hits += 1
    self.save()

def board():
    return None