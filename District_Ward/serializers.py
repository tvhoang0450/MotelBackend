from django import forms
from .models import District
from rest_framework import serializers

# from DichVu.models import DichVu
# from TinhTP.models import TinhTP

# from District.models import District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('idDistrict','DistrictName')