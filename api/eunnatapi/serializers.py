from rest_framework import serializers
from .models import Deptartment, Images

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deptartment
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"