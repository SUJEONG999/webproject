from django.db import models
from uuid import uuid4
from datetime import datetime
from django.contrib.auth.models import User

class Hospital(models.Model) :
    h_id = models.IntegerField(primary_key=True)
    h_name = models.CharField(max_length=50)
    h_address = models.CharField(max_length=50)
    h_type = models.CharField(max_length=50)
    h_number = models.IntegerField(null=True)


class Clinic(models.Model) :
    name = models.CharField(primary_key=True, max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField(null=True)


# 상원
class Restaurant(models.Model) :
    id = models.IntegerField(primary_key=True)
    r_si = models.CharField(max_length=10)
    r_gu = models.CharField(max_length=10)
    r_name = models.TextField()
    r_address = models.TextField()

# 하영
class Board(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    postname = models.CharField(max_length=50, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    mainphoto = models.ImageField(blank=True, null=True, verbose_name='사진')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

#관리자 페이지에서 정상적으로 title 테이블 출력
    def __str__(self):
        return self.title


@property
def click(self):
    self.hits += 1
    self.save()

def board():
    return None