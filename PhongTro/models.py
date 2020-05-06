from django.db import models

# Create your models here.
from django.utils import timezone

from DichVu.models import DichVu
from TinhTP.models import TinhTP
from HuyenQuan.models import HuyenQuan


class PhongTro(models.Model):
    owner = models.ForeignKey('auth.User', related_name='PhongTro', on_delete=models.CASCADE)
    DichVu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    TinhTP = models.ForeignKey(TinhTP, on_delete=models.CASCADE)
    TieuDe = models.CharField(max_length=100)
    Anh = models.ImageField(upload_to='', default='images.jpg')
    HuyenQuan = models.ForeignKey(HuyenQuan, on_delete=models.CASCADE)
    Gia = models.IntegerField(default=0)
    DiaChi = models.CharField(max_length=100)
    NgayDang = models.DateField(default=timezone.now)
    SDT = models.IntegerField(default=0)
    DienTich = models.IntegerField(default=0)
    NoiDung = models.CharField(max_length=1000)

    def __str__(self):
        return self.TieuDe