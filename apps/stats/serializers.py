from rest_framework import serializers


class EmoteSerializer(serializers.Serializer):
    emote = serializers.CharField(max_length=255)
    total = serializers.IntegerField()


class MentionSerializer(serializers.Serializer):
    mention = serializers.CharField(max_length=255)
    total = serializers.IntegerField()


class EmojiSerializer(serializers.Serializer):
    emoji = serializers.CharField(max_length=255)
    total = serializers.IntegerField()
