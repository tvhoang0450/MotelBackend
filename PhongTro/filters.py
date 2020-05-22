from .models import PhongTro

import django_filters


class PhongTroFilterSet(django_filters.FilterSet):
    class Meta:
        model = PhongTro
        fields = ['DichVu', 'province', 'district', 'ward', 'street', 'Gia', 'DienTich']
