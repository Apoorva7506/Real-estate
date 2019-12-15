from django.db import models
from datetime import datetime 

class Realtor(models.Model):
    name=models.CharField(max_length=40)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,null=True,)
    description=models.TextField(blank=True)
    contact=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Flats(models.Model):
    hname=models.CharField(max_length=70)
    city=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    realtor=models.ForeignKey(Realtor, on_delete=models.CASCADE)
    address=models.TextField()
    description=models.TextField(blank=True)
    rate=models.IntegerField()
    bedrooms=models.IntegerField()
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='media/h.jpg')
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='media/h.jpg')
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True,default='media/h.jpg')
    list_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.hname

