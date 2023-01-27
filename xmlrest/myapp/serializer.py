from rest_framework_xml.renderers import XMLRenderer
from rest_framework import  serializers
from rest_framework_xml.parsers import XMLParser
from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"