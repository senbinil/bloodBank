from django.urls import path

from location.views import getCity

app_name='location'
urlpatterns = [
    path('getDistrict/',getCity,name='getCity'),
]
