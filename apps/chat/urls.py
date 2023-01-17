from django.urls import path

from .views import ChatView, EmoteView

urlpatterns = [
    path("messages/", (ChatView.as_view({"get": "list"})), name="chat_messages"),
    path("emotes/", (EmoteView.as_view({"get": "list"})), name="chat_emotes"),
]
