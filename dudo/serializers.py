from rest_framework import serializers
from .models import *


class DeviceSer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"