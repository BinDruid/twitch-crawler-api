from django.db import models
from django.db.models import F, Count, Sum


class ChatManager(models.Manager):
    def by_emotes(self):
        return (
            Chat.objects.annotate(emote=F("emotes__emote__code"))
            .exclude(emote__isnull=True)
            .values("emote")
            .annotate(total=Sum("emotes__count"))
            .order_by("-total")
        )

    def by_emojis(self):
        return (
            Chat.objects.annotate(emoji=F("emojis__emoji"))
            .exclude(emoji__isnull=True)
            .values("emoji")
            .annotate(total=Sum("emojis__count"))
            .order_by("-total")
        )

    def by_mentions(self):
        return (
            Chat.objects.annotate(mention=F("mentions__mention"))
            .exclude(mention__isnull=True)
            .values("mention")
            .annotate(total=Sum("mentions__count"))
            .order_by("-total")
        )


class Chat(models.Model):

    """
    Description
    """

    objects = ChatManager()

    message = models.CharField(max_length=600)
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    is_sub = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-date",
        ]
        db_table = "chats"

    def __str__(self):
        return self.message


class Emote(models.Model):

    """
    Description
    """

    code = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    provider = models.CharField(max_length=10)
    set = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "code",
        ]
        db_table = "emotes"

    def __str__(self):
        return self.code


class MessageEmojis(models.Model):
    """
    Description
    """

    message = models.ForeignKey(Chat, related_name="emojis", on_delete=models.CASCADE)
    emoji = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "message_emojis"


class MessageEmotes(models.Model):
    """
    Description
    """

    message = models.ForeignKey(Chat, related_name="emotes", on_delete=models.CASCADE)
    emote = models.ForeignKey(Emote, on_delete=models.PROTECT)
    count = models.IntegerField()

    class Meta:
        db_table = "message_emotes"


class MessageMentions(models.Model):
    """
    Description
    """

    message = models.ForeignKey(Chat, related_name="mentions", on_delete=models.CASCADE)
    mention = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "message_mentions"
