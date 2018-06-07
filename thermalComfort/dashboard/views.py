from dashboard import urls
from rest_framework import (response, schemas, filters, generics, viewsets,
                            views)
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .models import (Floor, Room, Sensor, Measurement, RealTimeData,
                     ConsolidatedData)

from .serializers import (FloorSerializer, RoomSerializer, SensorSerializer,
                          MeasurementSerializer, RealTimeDataSerializer,
                          ConsolidatedDataSerializer)


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='ThermalComfort API Docs :: SQL',
                                        patterns=urls.api_url_patterns,
                                        url='/sql/api/v1/')
    return response.Response(generator.get_schema())


# CRUD
class FloorViewSet(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def create_realtimedata(self, request):
        pass


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()


class RealTimeDataViewSet(viewsets.ModelViewSet):
    serializer_class = RealTimeDataSerializer
    queryset = RealTimeData.objects.all()


class ConsolidatedDataViewSet(viewsets.ModelViewSet):
    serializer_class = ConsolidatedDataSerializer
    queryset = ConsolidatedData.objects.all()
