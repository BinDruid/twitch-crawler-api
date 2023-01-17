from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from django.shortcuts import get_object_or_404

# from .models import Chats, Emotes
# from .serializers import ChatSerializer, EmoteSerializer
