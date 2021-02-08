from django.db import models

class Hospital(models.Model) :
    region = models.CharField(max_length=50)
    h_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    h_type = models.CharField(max_length=50)
    number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.region)+","+str(self.h_name)+","+str(self.address)+\
               ","+str(self.h_type) + ","+(self.number)