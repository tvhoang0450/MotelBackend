from rest_framework import serializers
from .models import PhongTro

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan

from DichVu.serializers import DichVuSerializer
from TinhTP.serializers import TinhTPSerializer
from HuyenQuan.serializers import HuyenQuanSerializer


class PhongTroSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = PhongTro
        fields = (
            'DichVu', 'TinhTP', 'HuyenQuan', 'TieuDe', 'Gia', 'Anh', 'DiaChi', 'owner', 'NgayDang', 'SDT',
            'NoiDung',
            'DienTich')
        read_only_fields = ('created', 'updated')

    def to_representation(self, instance):
        self.fields['DichVu'] = DichVuSerializer(read_only=True)
        self.fields['TinhTP'] = TinhTPSerializer(read_only=True)
        self.fields['HuyenQuan'] = HuyenQuanSerializer(read_only=True)
        return super(PhongTroSerializer, self).to_representation(instance)
