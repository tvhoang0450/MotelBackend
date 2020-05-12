from django.db import models

# Create your models here.
from django.utils import timezone

# from TinhTP.models import TinhTP
from District_Ward.models import District
from District_Ward.models import Ward

class MotelTypes(models.Model):
    TypeMotel = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class Motel(models.Model):
    owner = models.ForeignKey('auth.User', related_name='PhongTro', on_delete=models.CASCADE)
    idType = models.ForeignKey(MotelTypes, on_delete=models.CASCADE, null=True)
    # TinhTP = models.ForeignKey(TinhTP, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='', default='images.jpg')
    idDistrict = models.ForeignKey(District, on_delete=models.CASCADE)
    idWard = models.ForeignKey(Ward, on_delete=models.CASCADE)
    Price = models.IntegerField(default=0)
    Address = models.CharField(max_length=100)
    PostDate = models.DateField(default=timezone.now)
    Update = models.DateField(default=timezone.now)
    NumberPhone = models.IntegerField(default=0)
    Area = models.IntegerField(default=0)
    Content = models.TextField(max_length=1000)

    def __str__(self):
        return self.Title




class Comments(models.Model):
    text = models.TextField(max_length=100)


# class Service(models.Model):
