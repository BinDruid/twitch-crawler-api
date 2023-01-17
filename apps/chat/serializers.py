from rest_framework import serializers
from .models import Emote, Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["username", "message", "date"]


class EmoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emote
        exclude = ("id",)
