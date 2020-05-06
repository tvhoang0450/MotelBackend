from django import forms
from .models import TinhTP
from rest_framework import serializers

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan


class TinhTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinhTP
        fields = ('TenTinh',)