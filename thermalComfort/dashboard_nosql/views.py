from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from pymongo import MongoClient

from dashboard_nosql import urls
from rest_framework import (response, schemas, filters, generics, viewsets,
                            views)
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import GenericAPIView
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(
                                title="ThermalComfort API Docs :: NOSQL",
                                patterns=urls.api_url_patterns,
                                url="/nosql/api/v1/")
    return response.Response(generator.get_schema())

# Create your views here.


class FloorReview(GenericAPIView):
    @api_view(["GET", "POST"])
    def floorsList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            floors = db["floors"]
            data = floors.find({})

            for dto in data:
                print(dto)
                json_data = {
                    "code": dto["code"],
                    "name": dto["name"],
                    "_id": str(dto["_id"]),
                    "_v": dto["_v"],
                    "rooms": dto["rooms"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)

        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            floors = db["floors"]
            data = JSONParser().parse(request)
            result = floors.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["PUT", "GET", "DELETE"])
    def floorsDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            floors = db["floors"]
            pk2 = int(pk)+1
            print(pk2)
            data = floors.find({"code": int(pk)})
            # data2 = JSONParser().parse(data)
            # print(data2)
            for dto in data:
                print(dto)
                json_data = {
                    "code": dto["code"],
                    "name": dto["name"],
                    "_v": dto["_v"],
                    "_id": str(dto["_id"]),
                    "rooms": dto["rooms"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "PUT":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            floors = db["floors"]
            d = JSONParser().parse(request)
            data = floors.update({"code": int(pk)}, {"name": d["name"], "code": d["code"], "rooms": d["rooms"], "_v":d["_v"]})
            respo = {
                "MongoObjectID": str(data),
                "Message": "Objeto actualizado"
            }
            client.close()
            return JsonResponse(respo, safe=False)
        elif request.method == "DELETE":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            floors = db["floors"]
            result = floors.remove({"code": int(pk)})
            respo = {
                "MongoObjectID": str(result),
                "Message": "Objeto eliminado"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["GET"])
    def floorRooms(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consData = db["rooms"]
            data = consData.find({"floor": int(pk)})
            for dto in data:
                json_data = {
                    "_id": str(dto["_id"]),
                    "floor": dto["floor"],
                    "code": dto["code"],
                    "name": dto["name"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)


class RoomSetViewer(GenericAPIView):
    @api_view(["GET", "POST"])
    def RoomList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            rooms = db["rooms"]
            data = rooms.find({})
            for dto in data:
                json_data = {
                    "code": dto["code"],
                    "name": dto["name"],
                    "floor": dto["floor"],
                    "_v": dto["_v"],
                    "_id": str(dto["_id"]),
                    "sensors": dto["sensors"],
                    "queries": dto["queries"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)

        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            rooms = db["rooms"]
            data = JSONParser().parse(request)
            code = data["code"]
            data['queries'] = 0
            result = rooms.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["GET", "PUT", "DELETE"])
    def RoomDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            rooms = db["rooms"]
            data = rooms.find({"code": int(pk)})
            for dto in data:
                json_data = {
                    "code": dto["code"],
                    "name": dto["name"],
                    "floor": dto["floor"],
                    "_v": dto["_v"],
                    "_id": str(dto["_id"]),
                    "sensors": dto["sensors"],
                    "queries": dto["queries"]
                }
                json_data["queries"] = json_data["queries"] + 1
                data = rooms.update({"code": int(json_data["code"])}, {"name": json_data["name"], "code": json_data["code"], "floor": json_data["floor"], "_v": json_data["_v"], "sensors":json_data["sensors"], "queries":json_data["queries"]})
                floors = db["floors"]
                floor_id = json_data["floor"]
                floorResult = floors.find({"code":int(floor_id)})
                for floor in floorResult:
                    floor_data = {
                        "code": floor["code"],
                        "name": floor["name"],
                        "_v": floor["_v"],
                        "_id": str(floor["_id"]),
                        "rooms": floor["rooms"]
                    }
                    result2 = []
                    rooms = rooms.find({}).sort("queries", -1).limit(2)
                    for room in rooms:
                        json = {
                            "code": room["code"],
                            "name": room["name"],
                            "floor": room["floor"],
                            "_v": room["_v"],
                            "_id": str(room["_id"]),
                            "sensors": room["sensors"],
                            "queries": room["queries"]
                        }
                        result2.append(json)
                    floor_data["rooms"] = result2
                    floors.update({"code": int(floor_data["code"])}, {"name": floor_data["name"], "code": floor_data["code"],  "_v":floor_data["_v"], "rooms":floor_data["rooms"]})
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "PUT":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            rooms = db["rooms"]
            d = JSONParser().parse(request)
            data = rooms.update({"code": int(pk)}, {"name": d["name"], "code": d["code"], "floor": d["floor"], "_v": d["_v"], "sensors":d["sensors"]})
            respo = {
                "MongoObjectID": str(data),
                "Message": "Objeto actualizado"
            }
            client.close()
            return JsonResponse(respo, safe=False)
        elif request.method == "DELETE":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            rooms = db["rooms"]
            result = rooms.remove({"code": int(pk)})
            respo = {
                "MongoObjectID": str(result),
                "Message": "Objeto eliminado"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["GET", "PUT", "DELETE"])
    def RoomMeasurement(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consData = db["consolidatedData"]
            data = consData.find({"room": int(pk)})
            for dto in data:
                json_data = {
                    "dateInit": dto["dateInit"],
                    "dateEnd": dto["dateEnd"],
                    "value": dto["value"],
                    "room": dto["room"],
                    "unit": dto["unit"],
                    "_v": dto["_v"],
                    "_id": str(dto["_id"])
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
    @api_view(["GET", "PUT", "DELETE"])
    def roomSensors(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consData = db["sensors"]
            data = consData.find({"room": int(pk)})
            for dto in data:
                json_data = {
                    "code": dto["code"],
                    "room": dto["room"],
                    "_v": dto["_v"],
                    "_id":str(dto["_id"])
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)


class SensorSetViewer(GenericAPIView):
    @api_view(["GET", "POST"])
    def SensorList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            sensors = db["sensors"]
            data = sensors.find({})
            for dto in data:
                json_data = {
                    "code": dto["code"],
                    "room": dto["room"],
                    "_v": dto["_v"],
                    "_id":str(dto["_id"])
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            sensors = db["sensors"]
            data = JSONParser().parse(request)
            result = sensors.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["GET"])
    def SensorDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            sensors = db["sensors"]
            data = sensors.find({"code": str(pk)})
            for dto in data:
                json_data = {
                    "code": dto["code"],
                    "room": dto["floor"],
                    "_v": dto["_v"],
                    "_id": str(dto["_id"])
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)

        elif request.method == "DELETE":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            sensors = db["sensors"]
            result = sensors.remove({"code": str(pk)})
            respo = {
                "MongoObjectID": str(result),
                "Message": "Objeto eliminado"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    def sensorMeasurement(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consData = db["measurements"]
            data = consData.find({"sensor": int(pk)})
            for dto in data:
                json_data = {
                    "name": dto["name"],
                    "unit": dto["unit"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)

    def sensorRealTimeData(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consData = db["realTimeData"]
            data = consData.find({"sensor": int(pk)})
            for dto in data:
                json_data = {
                    "date": dto["date"],
                    "value": dto["value"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)


class MeasurementSetViewer(GenericAPIView):
    @api_view(["GET", "POST"])
    def measurementList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            measurements = db["measurements"]
            data = measurements.find({})
            for dto in data:
                json_data = {
                    "name": dto["name"],
                    "unit": dto["unit"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            measurements = db["measurements"]
            data = JSONParser().parse(request)
            result = measurements.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["PUT", "GET", "DELETE"])
    def measurementDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            measurements = db["measurements"]
            data = measurements.find({"_id": str(pk)})
            for dto in data:
                json_data = {
                    "name": dto["name"],
                    "unit": dto["unit"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)


class RealTimeDataSetViewer(GenericAPIView):
    @api_view(["GET", "POST"])
    def realTimeDataList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            realTData = db["realTimeData"]
            data = realTData.find({})
            for dto in data:
                json_data = {
                    "date": dto["date"],
                    "value": dto["value"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            realTData = db["realTimeData"]
            data = JSONParser().parse(request)
            result = realTData.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["PUT", "GET", "DELETE"])
    def realTimeDataDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            realTData = db["realTimeData"]
            data = realTData.find({"_id": str(pk)})
            for dto in data:
                json_data = {
                    "date": dto["date"],
                    "value": dto["value"],
                    "sensor": dto["sensor"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)


class ConsolidatedDataSetViewer(GenericAPIView):
    @api_view(["GET", "POST"])
    def consolidatedDataList(request):
        result = []
        if request.method == "GET":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consolidatedData = db["consolidatedData"]
            data = consolidatedData.find({})
            for dto in data:
                json_data = {
                    "dateInit": dto["dateInit"],
                    "dateEnd": dto["dateEnd"],
                    "value": dto["value"],
                    "room": dto["room"],
                    "unit": dto["unit"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
        elif request.method == "POST":
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consolidatedData = db["consolidatedData"]
            data = JSONParser().parse(request)
            result = consolidatedData.insert(data)
            respo = {
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    @api_view(["PUT", "GET", "DELETE"])
    def consolidatedDataDetail(request, pk, format=None):
        if request.method == "GET":
            result = []
            client = MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
            db = client[settings.MONGODB_DB]
            consolidatedData = db["consolidatedData"]
            data = consolidatedData.find({"_id": str(pk)})
            for dto in data:
                json_data = {
                    "dateInit": dto["dateInit"],
                    "dateEnd": dto["dateEnd"],
                    "value": dto["value"],
                    "room": dto["room"],
                    "unit": dto["unit"],
                    "_v": dto["_v"]
                }
                result.append(json_data)
            client.close()
            return JsonResponse(result, safe=False)
