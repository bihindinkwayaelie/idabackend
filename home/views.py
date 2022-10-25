from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Sendmoney
from .models import Registration
from .models import Loan
from .serializers import *
from django.http import Http404 #to treat not found 
from rest_framework.views import APIView #Apiview class
from rest_framework.response import Response #response
from rest_framework import status #status code

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

class LoanApi(APIView):
    def get(self, request, format=None):
        loan = Loan.objects.all()
        serializer = LoanSerializer(loan, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanApiDetail(APIView):
    def get_object(self, pk):
        try:
            return Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loan = self.get_object(pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)