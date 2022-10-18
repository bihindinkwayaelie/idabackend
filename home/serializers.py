from rest_framework import serializers
from .models import *

class SendmoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sendmoney 
        fields = ['amount','sender','receiver','receiverPhone','created']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration 
        fields = ['sender','email','phone']