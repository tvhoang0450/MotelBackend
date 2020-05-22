from rest_framework import serializers

from .models import province, district, street, ward


class provinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = province
        fields = ('_name',)


class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = ('_name',)


class wardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ward
        fields = ('_name',)


class streetSerializer(serializers.ModelSerializer):
    class Meta:
        model = street
        fields = ('_name',)

