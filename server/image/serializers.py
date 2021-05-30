from rest_framework import serializers
from .models import ImageManager

class ImageManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageManager
        fields = '__all__'