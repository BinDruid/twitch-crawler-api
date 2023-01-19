from rest_framework import serializers


class EmoteSerializer(serializers.Serializer):
    emote = serializers.CharField(max_length=255)
    url = serializers.CharField(max_length=255)
    total = serializers.IntegerField()


class MentionSerializer(serializers.Serializer):
    mention = serializers.CharField(max_length=255)
    total = serializers.IntegerField()


class EmojiSerializer(serializers.Serializer):
    emoji = serializers.CharField(max_length=255)
    total = serializers.IntegerField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    message_counts = serializers.IntegerField()


class DaySerializer(serializers.Serializer):
    day = serializers.DateTimeField()
    message_counts = serializers.IntegerField()


serializers = {
    "emote": EmoteSerializer,
    "emoji": EmojiSerializer,
    "mention": MentionSerializer,
    "user": UserSerializer,
    "day": DaySerializer,
}
