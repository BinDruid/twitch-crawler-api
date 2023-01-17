from django.db import models


class Chats(models.Model):

    """
    Description
    """

    message = models.CharField(max_length=600)
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    is_sub = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "date",
        ]
        db_table = "chats"

    def __str__(self):
        return self.message


class Emotes(models.Model):

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
            "date",
        ]
        db_table = "emotes"

    def __str__(self):
        return self.code


class MessageEmojis(models.Model):
    """
    Description
    """

    message = models.ForeignKey(Chats, related_name="emojis", on_delete=models.CASCADE)
    emoji = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "message_emojis"


class MessageEmotes(models.Model):
    """
    Description
    """

    message = models.ForeignKey(Chats, related_name="emotes", on_delete=models.CASCADE)
    emote = models.ForeignKey(Emotes, on_delete=models.PROTECT)
    count = models.IntegerField()

    class Meta:
        db_table = "message_emotes"


class MessageMentions(models.Model):
    """
    Description
    """

    message = models.ForeignKey(
        Chats, related_name="mentions", on_delete=models.CASCADE
    )
    mention = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table = "message_mentions"
