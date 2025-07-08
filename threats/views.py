from rest_framework import generics, filters
from .models import Threat
from .serializers import ThreatSerializer
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ThreatListView(generics.ListAPIView):
    serializer_class = ThreatSerializer
    queryset = Threat.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cleaned_description']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(threat_category=category)
        return queryset

class ThreatDetailView(generics.RetrieveAPIView):
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
    lookup_field = 'id'

class ThreatStatsView(APIView):
    def get(self, request):
        total = Threat.objects.count()
        category_count = Threat.objects.values('threat_category').annotate(count=Count('id'))
        severity_count = Threat.objects.values('severity_score').annotate(count=Count('id'))

        return Response({
            'total_threats': total,
            'category_counts': category_count,
            'severity_counts': severity_count
        })
