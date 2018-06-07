from django.contrib import admin
from .models import (Floor, Room, Sensor, Measurement, RealTimeData,
                     ConsolidatedData)


# Register your models here.
@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'floor')


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'room', 'measurement')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit')


@admin.register(RealTimeData)
class RealTimeDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'sensor', 'value')


@admin.register(ConsolidatedData)
class ConsolidatedDataDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateInit', 'dateEnd', 'measurement', 'room')
