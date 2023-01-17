from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from django.shortcuts import get_object_or_404
from .models import Chats, Emotes
from .serializers import ChatSerializer, EmoteSerializer


class ChatView(ModelViewSet):
    queryset = Chats.objects.all()

    def get_serializer_class(self):
        return ChatSerializer


class EmoteView(ModelViewSet):
    queryset = Emotes.objects.all()

    def get_serializer_class(self):
        return EmoteSerializer
