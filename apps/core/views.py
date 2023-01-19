from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response


class ApiRootView(APIView):
    """
    Lists currently avaiable endpoints.
    """

    def get(self, request, format=None):
        return Response(
            {
                "messages": reverse("chat_messages", request=request, format=format),
                "emotes": reverse("chat_emotes", request=request, format=format),
                "stats": reverse("pivotal_stats", request=request, format=format),
            }
        )
