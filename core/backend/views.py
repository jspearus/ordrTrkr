from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializers import OrderRecordSerializer, StoreTimesSerializer
from.models import OrderRecord, StoreTimes

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
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
    