from django.db import models

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