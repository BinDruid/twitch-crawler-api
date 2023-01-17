from django.contrib import admin

from .models import Chat, Emote


@admin.register(Chat)
class ChatsAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ["message", "user_id"]


@admin.register(Emote)
class EmotesAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ["code", "url"]
