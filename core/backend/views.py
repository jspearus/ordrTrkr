from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializers import OrderRecordSerializer, StoreTimesSerializer
from.models import OrderRecord, StoreTimes

class OrderRecordViewSet(viewsets.ModelViewSet):
    queryset = OrderRecord.objects.all()
    serializer_class = OrderRecordSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('store_number', 'lane_number', 'time_started', 'time_finished')
    
class StoreTimesViewSet(viewsets.ModelViewSet):
    queryset = StoreTimes.objects.all()
    serializer_class = StoreTimesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('store_number', 'hour_due')