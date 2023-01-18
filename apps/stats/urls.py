from django.urls import path
from .views import UserMessage

urlpatterns = [
    path("users/", UserMessage.as_view({"get": "list"}), name="message_by_user"),
]
