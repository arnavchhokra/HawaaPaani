from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class WQISerializer(ModelSerializer):
    class Meta:
        model = WQI
        fields = "__all__"


class AQISerializer(ModelSerializer):
    class Meta:
        model = AQI
        fields = "__all__"
