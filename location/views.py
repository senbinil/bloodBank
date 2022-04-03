from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from location.models import District,City

# Create your views here.

def getCity(request):
    district=request.GET['district']
    result=[]
    district=str(district)
    try:
        selectDistrict=District.objects.get(name=district)
        all_cities=selectDistrict.city_set.all()
        for city in all_cities:
            result.append({'name':city.name})
    except:
        result=[]
    return HttpResponse(JsonResponse(result,safe=False))
