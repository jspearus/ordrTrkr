from django.contrib import admin
from .models import OrderRecord, StoreTimes

# Register your models here.
admin.site.register(OrderRecord)
admin.site.register(StoreTimes)