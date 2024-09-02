from rest_framework import serializers
from .models import *

class ZUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZUser
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'