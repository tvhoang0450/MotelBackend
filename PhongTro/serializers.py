from rest_framework import serializers
from .models import PhongTro

from DichVu.models import DichVu

from DichVu.serializers import DichVuSerializer
from DiaChi.serializers import provinceSerializer, districtSerializer, wardSerializer, streetSerializer


class PhongTroSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = PhongTro
        fields = (
            'DichVu', 'province', 'district', 'ward', 'street', 'TieuDe', 'Gia', 'Anh', 'owner', 'NgayDang',
            'SDT',
            'NoiDung',
            'DienTich')
        read_only_fields = ('created', 'updated')

    def to_representation(self, instance):
        self.fields['DichVu'] = DichVuSerializer(read_only=True)
        self.fields['province'] = provinceSerializer(read_only=True)
        self.fields['district'] = districtSerializer(read_only=True)
        self.fields['ward'] = wardSerializer(read_only=True)
        self.fields['street'] = streetSerializer(read_only=True)
        return super(PhongTroSerializer, self).to_representation(instance)
