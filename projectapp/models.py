from django.db import models
from uuid import uuid4
from datetime import datetime

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
    no = models.IntegerField(primary_key=True)
    store = models.CharField(max_length=30, verbose_name='방문매장')
    satisfaction = models.PositiveIntegerField(default=5, verbose_name='만족도')
    title = models.CharField(max_length=128, default="제목", verbose_name='제목')
    content = models.TextField(default="내용", verbose_name='내용')

#관리자 페이지에서 정상적으로 title 테이블 출력
    def __str__(self):
        return self.title


@property
def click(self):
    self.hits += 1
    self.save()

def board():
    return None