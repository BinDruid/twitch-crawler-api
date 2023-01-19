from django.urls import path
from .views import ReportStats

urlpatterns = [
    path("", ReportStats.as_view({"get": "list"}), name="pivotal_stats"),
]
