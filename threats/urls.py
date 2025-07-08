from django.urls import path
from .views import ThreatListView, ThreatDetailView, ThreatStatsView

urlpatterns = [
    path('threats', ThreatListView.as_view()),
    path('threats/<int:id>', ThreatDetailView.as_view()),
    path('threats/stats', ThreatStatsView.as_view()),
]
