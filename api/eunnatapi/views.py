from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Deptartment, Images
from .serializers import DepartmentSerializer
from drf_spectacular.utils import extend_schema


# Create your views here.

class DepartmentView(viewsets.ViewSet):
    """
    For viewing all Departments
    """

    queryset = Deptartment.objects.all()

    @extend_schema(responses=DepartmentSerializer)
    def list(self, request):
        serializer = DepartmentSerializer(self.queryset, many=True)
        return Response(serializer.data)
