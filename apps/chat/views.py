from rest_framework.viewsets import ModelViewSet
from .models import Chat, Emote
from .serializers import ChatSerializer, EmoteSerializer


class ChatView(ModelViewSet):
    queryset = Chat.objects.all()

    def get_serializer_class(self):
        return ChatSerializer


class EmoteView(ModelViewSet):
    queryset = Emote.objects.all()

    def get_serializer_class(self):
        return EmoteSerializer
