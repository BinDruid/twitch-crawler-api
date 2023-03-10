# Generated by Django 4.1.5 on 2023-01-17 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=600)),
                ("username", models.CharField(max_length=255)),
                ("user_id", models.IntegerField()),
                ("is_sub", models.BooleanField(default=False)),
                ("is_mod", models.BooleanField(default=False)),
                ("is_vip", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "chats",
                "ordering": ["date"],
            },
        ),
        migrations.CreateModel(
            name="Emotes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
                ("provider", models.CharField(max_length=10)),
                ("set", models.CharField(max_length=10)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "emotes",
                "ordering": ["date"],
            },
        ),
        migrations.CreateModel(
            name="MessageMentions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mention", models.CharField(max_length=255)),
                ("count", models.IntegerField()),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mentions",
                        to="chat.chats",
                    ),
                ),
            ],
            options={
                "db_table": "message_mentions",
            },
        ),
        migrations.CreateModel(
            name="MessageEmotes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField()),
                (
                    "emote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="chat.emotes"
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emotes",
                        to="chat.chats",
                    ),
                ),
            ],
            options={
                "db_table": "message_emotes",
            },
        ),
        migrations.CreateModel(
            name="MessageEmojis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emoji", models.CharField(max_length=255)),
                ("count", models.IntegerField()),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emojis",
                        to="chat.chats",
                    ),
                ),
            ],
            options={
                "db_table": "message_emojis",
            },
        ),
    ]
