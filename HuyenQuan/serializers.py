from django import forms
from .models import HuyenQuan
from rest_framework import serializers

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan


class HuyenQuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuyenQuan
        fields = ('TenHuyen',)