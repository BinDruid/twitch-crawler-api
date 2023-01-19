from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.chat.models import Chat
from .serializers import serializers


class ReportStats(ReadOnlyModelViewSet):
    page_size = 10
    serializer_classes = serializers

    queryset_classes = {
        "emote": Chat.objects.by_emote(),
        "emoji": Chat.objects.by_emoji(),
        "mention": Chat.objects.by_mention(),
        "user": Chat.objects.by_user(),
        "day": Chat.objects.by_day(),
    }

    def get_serializer_class(self, pivot):
        return self.serializer_classes[pivot]

    def get_queryset(self):
        return self.queryset_classes

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class(kwargs["pivot"])
        kwargs.pop("pivot", None)
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        querysets = self.get_queryset()

        serializers = {
            pivot: self.get_serializer(queryset, many=True, pivot=pivot)
            for pivot, queryset in querysets.items()
        }
        response = Response(
            {
                "results": {
                    pivot: serializer.data[: self.page_size]
                    for pivot, serializer in serializers.items()
                }
            }
        )
        return response
