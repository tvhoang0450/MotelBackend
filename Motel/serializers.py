from rest_framework import serializers
from .models import Motel

# from DichVu.models import DichVu
# from TinhTP.models import TinhTP

from District_Ward.models import District
from District_Ward.models import Ward
# from DichVu.serializers import DichVuSerializer
# from TinhTP.serializers import TinhTPSerializer
from District_Ward.serializers import DistrictSerializer


class MotelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='users.username')

    class Meta:
        model = Motel
        fields = (
            'idDistrict', 'Title', 'Price', 'Image', 'Address', 'owner', 'PostDate', 'NumberPhone',
            'Content',
            'Area')
        read_only_fields = ('created', 'updated')

    def to_representation(self, instance):
        self.fields['idDistrict'] = DistrictSerializer(read_only=True)
        return super(DistrictSerializer, self).to_representation(instance)
