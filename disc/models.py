from django.db import models

# Create your models here.
class Movies(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Booking(models.Model):
    cs_name=models.CharField(max_length=255)
    cs_phno=models.CharField(max_length=255)
    name=models.ForeignKey(Movies,on_delete=models.CASCADE)
    def __str__(self):
        return self.cs_name
    
class Contact(models.Model):
    c_name=models.CharField(max_length=255)
    c_phone=models.CharField(max_length=255)
    c_email=models.EmailField()
    def __str__(self):
        return self.c_name
    