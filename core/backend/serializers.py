from rest_framework import serializers
from .models import OrderRecord, StoreTimes

class OrderRecordSerializer(serializers.ModelSerializer):
    model = OrderRecord
    class Meta:
        model = OrderRecord
        fields = ('id', 'palets', 'number_of_cases', 'aile_numbers','store_number', 'lane_number', 'time_started', 'time_finished')
    
class StoreTimesSerializer(serializers.ModelSerializer):
   model = StoreTimes
   class Meta:
       model = StoreTimes
       fields = ('id','store_number', 'hour_due')
   
    