from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Count, Sum
from django.shortcuts import get_object_or_404
from apps.chat.models import Chat, Emote
from .serializers import EmoteSerializer, EmojiSerializer, MentionSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class UserMessage(viewsets.ReadOnlyModelViewSet):
    # pagination_class = StandardResultsSetPagination

    @property
    def pivot(self):
        return self.request.GET.get("pivot", "emote")

    @property
    def serializer_for_pivot(self):
        serializer_classes = {
            "emote": EmoteSerializer,
            "emoji": EmojiSerializer,
            "mention": MentionSerializer,
        }
        return serializer_classes[self.pivot]

    @property
    def queryset_for_pivot(self):
        queryset_classes = {
            "emote": Chat.objects.by_emotes(),
            "emoji": Chat.objects.by_emojis(),
            "mention": Chat.objects.by_mentions(),
        }
        return queryset_classes[self.pivot]

    def get_serializer_class(self):
        return self.serializer_for_pivot

    def get_queryset(self):
        return self.queryset_for_pivot
