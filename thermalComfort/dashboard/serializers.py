from rest_framework import serializers

from .models import (Floor, Room, Sensor, Measurement, RealTimeData,
                     ConsolidatedData)


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class RealTimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTimeData
        fields = '__all__'


class ConsolidatedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidatedData
        fields = '__all__'
