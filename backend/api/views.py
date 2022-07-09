from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import TikiNgonItem
from api.serializers import TikiNgonItemSerializer

# Create your views here.
@csrf_exempt
def tikingonItemApi(request, id=0):
    if request.method=='GET':
        tikingonitem = TikiNgonItem.objects.all()
        tikingonitem_serializer = TikiNgonItemSerializer(tikingonitem, many=True)
        return JsonResponse(tikingonitem_serializer.data, safe=False)
    elif request.method=='POST':
        pass
    elif request.method=='PUT':
        pass
        # tikingonitem_data = JSONParser().parse(request)
        # tikingonitem_serializer = TikiNgonItemSerializer(data= tikingonitem_data)
    elif request.method=='DELETE':
        pass
