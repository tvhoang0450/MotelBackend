from .models import baseInforMotel

import django_filters


class PhongTroFilterSet(django_filters.FilterSet):
    class Meta:
        model = baseInforMotel
        fields = ['typeMotel', 'district', 'ward', 'price', 'areas']
