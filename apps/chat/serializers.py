from rest_framework import serializers
from .models import Emotes, Chats


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = "__all__"


class EmoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotes
        fields = "__all__"
