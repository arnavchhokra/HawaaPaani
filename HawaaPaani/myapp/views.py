from django.shortcuts import render

from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def AQI_ALL(request):
    AQI_All = AQI.objects.all()
    serializer = AQISerializer(AQI_All, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def AQI_Detail(request, state):
    try:
        aqi_details = AQI.objects.get(STATE=state)
    except AQI.DoesNotExist:
        return Response(
            {"detail": "AQI data for the specified state not found."}, status=404
        )

    serializer = AQISerializer(aqi_details)
    return Response(serializer.data)


@api_view(["GET"])
def WQI_ALL(request):
    WQI_All = WQI.objects.all()
    serializer = WQISerializer(WQI_All, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def WQI_Detail(request, state):
    try:
        wqi_details = WQI.objects.get(STATE=state)
    except WQI.DoesNotExist:
        return Response(
            {"detail": "WQI data for the specified state not found."}, status=404
        )

    serializer = WQISerializer(wqi_details)
    return Response(serializer.data)
