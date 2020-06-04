from rest_framework import serializers

from .models import Province, District, Street, Ward


class provinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('_name',)


class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('_name',)


class wardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ('_name',)


class streetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('_name',)

