from django.conf.urls import url, include

from .views import FloorReview, schema_view, RoomSetViewer, SensorSetViewer, MeasurementSetViewer, RealTimeDataSetViewer, ConsolidatedDataSetViewer

api_url_patterns = [
    url(r'^floors/$', FloorReview.floorsList),
    url(r'^floors/(?P<pk>[0-9]+)$', FloorReview.floorsDetail),
    url(r'^floors/(?P<pk>[0-9]+)/rooms/',
        FloorReview.floorRooms),
    url(r'^rooms/$', RoomSetViewer.RoomList),
    url(r'^rooms/(?P<pk>[0-9]+)/measurements/',
        RoomSetViewer.RoomMeasurement),
    url(r'^rooms/(?P<pk>[0-9]+)/sensors/',
        RoomSetViewer.roomSensors),
    url(r'^rooms/(?P<pk>[0-9]+)$', RoomSetViewer.RoomDetail),
    url(r'^sensors/$', SensorSetViewer.SensorList),
    url(r'^sensors/(?P<pk>[0-9]+)$', SensorSetViewer.SensorDetail),
    url(r'^sensors/(?P<pk>[0-9]+)/measurements/',
        SensorSetViewer.sensorMeasurement),
    url(r'^sensors/(?P<pk>[0-9]+)/realtimedata/',
        SensorSetViewer.sensorRealTimeData),
    url(r'^measurements/$', MeasurementSetViewer.measurementList),
    url(r'^measurements/(?P<pk>[0-9]+)$',
        MeasurementSetViewer.measurementDetail),
    url(r'^realtimedata/$', RealTimeDataSetViewer.realTimeDataList),
    url(r'^realtimedata/(?P<pk>[0-9]+)$',
        RealTimeDataSetViewer.realTimeDataDetail),
    url(r'^consolidateddata/$', ConsolidatedDataSetViewer.consolidatedDataList),
    url(r'^consolidateddata/(?P<pk>[0-9]+)$',
        ConsolidatedDataSetViewer.consolidatedDataDetail)
]

urlpatterns = [
    url(r'^api/v1/', include(api_url_patterns)),
    url(r'^docs/', schema_view),
]
