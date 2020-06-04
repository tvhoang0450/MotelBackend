from django.db import models

# Create your models here.
from django.utils import timezone

from local.models import District, Ward
from profile_user.models import User


class TypeMotel(models.Model):
    nameType = models.CharField(max_length=50)

    def __str__(self):
        return self.nameType


class baseInforMotel(models.Model):  # thông tin cơ bản 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    typeMotel = models.ForeignKey(TypeMotel, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    areas = models.IntegerField(default=0)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title


class Service(models.Model):
    motel = models.OneToOneField(baseInforMotel, on_delete=models.CASCADE)
    parking = models.BooleanField(default=False) #chỗ đỗ xe
    wifi = models.BooleanField(default = False) # internet miễn phí
    washing_machine = models.BooleanField(default = False) # máy giặt
    air_condition = models.BooleanField(default = False)  # máy lạnh
    yard = models.BooleanField(default = False) #sân phơi đồ
    PCCC = models.BooleanField(default = False) # an toàn phòng cháy chữa cháy
    elevator = models.BooleanField(default = False)  # thang máy
    
    def __str__(self):
        return self.board.motel.title


class Board(models.Model):  # bảng nội dung chi tiết bài đăng và hình ảnh
    motel = models.OneToOneField(baseInforMotel, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.motel.title



class ImageMotel(models.Model):
    motel = models.ForeignKey(baseInforMotel, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'motel/')
    def __str__(self):
        return self.board.motel.title