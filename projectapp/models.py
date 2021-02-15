# 하영
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    # writer = models.ForeignKey('auth.user', on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    # store = models.CharField(max_length=30, verbose_name='방문매장')
    # visited_date = models.DateTimeField(verbose_name='방문일자')
    # customers = models.CharField(max_length=30, default="가족", verbose_name='동반고객')
    # satisfaction = models.PositiveIntegerField(default=5, verbose_name='만족도')
    # title = models.CharField(max_length=128, default="제목", verbose_name='제목')
    # content = models.TextField(default="내용", verbose_name='내용')
    # hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    # stars = models.PositiveIntegerField(default=0, verbose_name='추천수')
    # created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='작성 시간')
    # modified_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='수정 시간')
    # upload_files = models.ImageField(blank=True, null=True, verbose_name='파일')
    # filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    postname = models.CharField(max_length=50, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    mainphoto = models.ImageField(blank=True, null=True, verbose_name='사진')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname