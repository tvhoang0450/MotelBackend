from django.db import models

# Create your models here.
# from TinhTP.models import TinhTP


class District(models.Model):
    DistrictName = models.CharField(max_length=100)
    # TinhTP = models.ForeignKey(TinhTP, on_delete=models.CASCADE)

    def __str__(self):
        return self.DistrictName

class Ward(models.Model):
    idDistrict = models.ForeignKey(District, on_delete=models.CASCADE)
    WardName = models.CharField(max_length=100)
    def __str__(self):
        return self.WardName