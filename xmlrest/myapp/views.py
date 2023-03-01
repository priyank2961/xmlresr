from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework.mixins import *
from rest_framework_xml.renderers import XMLRenderer
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import *
from json import loads
from json2xml import json2xml
import xmltodict,dicttoxml

from rest_framework.views import APIView
import requests

class CustomViewSet(ListModelMixin,RetrieveModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = [XMLParser]
    renderer_classes = [XMLRenderer]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"msg":"student deleted successfully"},status=status.HTTP_202_ACCEPTED)
    
class CallXml(APIView):

    def get(self,request,format = None):
        x = requests.get('http://127.0.0.1:8000/student')
        x = xmltodict.parse(x.text)
        return Response(x)
    
    def post(self,request,format = None):
        headers = {'Content-Type': 'application/xml'} 
        # x = requests.post('http://127.0.0.1:8000/student',data=json2xml.Json2xml(request.data).to_xml(),headers=headers)
        x = xmltodict.parse(x.text)
        # return Response() 
        return Response(x)
    
    def put(self, request, pk, format=None):
        print("not here")
        headers = {'Content-Type': 'application/xml'} 
        x = requests.put(f'http://127.0.0.1:8000/student/{pk}/',data=json2xml.Json2xml(request.data).to_xml(),headers=headers)
        x = xmltodict.parse(x.text)
        # return Response() 
        return Response(x)
    
    def patch(self, request, pk, format=None):
        headers = {'Content-Type': 'application/xml'} 
        x = requests.patch(f'http://127.0.0.1:8000/student/{pk}/',data=json2xml.Json2xml(request.data).to_xml(),headers=headers)
        x = xmltodict.parse(x.text)
        # return Response() 
        return Response(x)
    
    def delete(self, request, pk, format=None):
        headers = {'Content-Type': 'application/xml'} 
        x = requests.delete(f'http://127.0.0.1:8000/student/{pk}/',headers=headers)
        x = xmltodict.parse(x.text)
        # return Response() 
        return Response(x)