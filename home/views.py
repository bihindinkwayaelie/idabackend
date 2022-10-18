from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Sendmoney
from .models import Registration
from .serializers import *

# Create your views here.
@csrf_exempt 
def sendmoney(request):
    if request.method == 'GET':
        sendnow = Sendmoney.objects.all()
        serializer = SendmoneySerializer(sendnow, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SendmoneySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt 
def sendoneyDetail(request, pk):
    try:
        onesend= Sendmoney.objects.get(pk=pk)
    except Sendmoney.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SendmoneySerializer( onesend )
        return JsonResponse(serializer.data)
    
    elif request.method =='PUT':
        data =JSONParser().parse(request)
        serializer = SendmoneySerializer(onesend, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    elif request.method == "DELETE":
        onesend.delete()
        return JsonResponse({'message':'delete succfhfd'}, status=201)
@csrf_exempt 
def Regist(request):
    if request.method == 'GET':
        getregistration = Registration.objects.all()
        serialreg = RegistrationSerializer(getregistration, many=True)
        return JsonResponse(serialreg.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)