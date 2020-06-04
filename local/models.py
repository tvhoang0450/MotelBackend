from django.db import models


# Create your models here.

class Province(models.Model):
    _name = models.CharField(max_length=50)
    _code = models.CharField(max_length=20)

    def __str__(self):
        return self._name


class District(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self._name


class Street(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(Province, on_delete=models.CASCADE)
    _district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self._name


class Ward(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(Province, on_delete=models.CASCADE)
    _district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self._name
