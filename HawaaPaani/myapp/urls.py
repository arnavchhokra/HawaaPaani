from django.urls import path
from . import views


urlpatterns = [
    path("aqi/all", views.AQI_ALL, name="events-list"),
    path("aqi/<str:state>/", views.AQI_Detail, name="events-detail"),
    path("wqi/all", views.WQI_ALL, name="events-list"),
    path("wqi/<str:state>", views.WQI_Detail, name="events-detail"),
]
