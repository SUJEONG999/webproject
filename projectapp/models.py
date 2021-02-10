from django.db import models

class Hospital(models.Model) :
    name = models.CharField(primary_key=True, max_length=50)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name + "," + (self.address) + "," + (self.type) + ","+str(self.number)

class Clinic(models.Model) :
    name = models.CharField(primary_key=True, max_length=50)
    address = models.CharField(max_length=50)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name + "," + (self.address) + "," + str(self.number)