from django.conf.urls import url, include
from .views import (schema_view, FloorViewSet, RoomViewSet, MeasurementViewSet,
                    SensorViewSet, RealTimeDataViewSet,
                    ConsolidatedDataViewSet)


api_url_patterns = [
    url(r'^floors/$', FloorViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='floor-list'),
    url(r'^floors/(?P<pk>[0-9]+)/$', FloorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='floor'),
    url(r'^rooms/$', RoomViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='room-list'),
    url(r'^rooms/(?P<pk>[0-9]+)/$', RoomViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='room'),
    url(r'^sensors/$', SensorViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='sensor-list'),
    url(r'^sensors/(?P<pk>[0-9]+)/$', SensorViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='sensor'),
    url(r'^sensors/(?P<code>w+)/realtimedata/$', SensorViewSet.as_view({
        'post': 'create_realtimedata'
    }), name='sensor-data'),
    url(r'^measurements/$', MeasurementViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='measurement-list'),
    url(r'^measurements/(?P<pk>[0-9]+)/$', MeasurementViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='measurement'),
    url(r'^realtimedatas/$', RealTimeDataViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='realtimedata-list'),
    url(r'^realtimedatas/(?P<pk>[0-9]+)/$', RealTimeDataViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='realtimedata'),
    url(r'^consolidateddatas/$', ConsolidatedDataViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='consolidateddatas-list'),
    url(r'^consolidateddatas/(?P<pk>[0-9]+)/$', ConsolidatedDataViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='consolidateddatas'),
]

urlpatterns = [
    url(r'^api/v1/', include(api_url_patterns)),
    url(r'^docs/', schema_view),
]
