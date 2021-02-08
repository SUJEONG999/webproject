from django.db import models

class Hospital(models.Model) :
    id = models.IntegerField(primary_key=True, serialize=False)
    region = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.id+","+str(self.region)+","+str(self.h_name)+","+str(self.address)+\
               ","+str(self.h_type) + ","+(self.number)