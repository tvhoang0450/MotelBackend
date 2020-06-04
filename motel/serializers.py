
from rest_framework import serializers

from rest_framework import serializers
from .models import TypeMotel, baseInforMotel, Service, Board, ImageMotel

from local.serializers import provinceSerializer, districtSerializer, wardSerializer, streetSerializer


class TypeMotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMotel
        fields = ('nameType',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMotel
        fields = ('image',)

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('content', 'address')    


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('parking','wifi','washing_machine','air_condition','yard','PCCC','elevator',)    


class MotelSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='users.username')
    images = ImageSerializer(many=True)
    noidung = ContentSerializer()
    # service = ServiceSerializer()
    class Meta:
        model = baseInforMotel
        fields = (
            'typeMotel', 'district', 'ward', 'Title', 'price', 'areas', 'created_at', 'updated_at', 
            'content',
            # 'service',
            'images')
        read_only_fields = ('created_at', 'updated_at')

    def to_representation(self, instance):
        self.fields['typeMotel'] = TypeMotelSerializer(read_only=True)
        self.fields['district'] = districtSerializer(read_only=True)
        self.fields['ward'] = wardSerializer(read_only=True)
        return super(MotelSerializer, self).to_representation(instance)

    def create(self, validated_data):
        arrimages = validated_data.pop('images')
        content = validated_data.pop('content')
        # services = validated_data.pop('service')

        motel = super(MotelSerializer, self).create(**validated_data)
        Board.objects.create(motel = motel, **content)
        # Service.objects.create(motel = motel, **services)
        for image in arrimages:
            ImageMotel.objects.create(motel = motel, image = image)
        return motel
