from django.http import HttpResponse
from .models import ImageManager
from .serializers import ImageManagerSerializer
from django.conf import settings
from rest_framework import generics
import json
import os

def create(request):
    print(request)
    params = json.loads(request.body.decode())
    print(params)
    img_name = ImageManager.create(params)
    img_url = request._current_scheme_host + settings.MEDIA_URL + 'results/' + img_name
    print(img_url)
    return HttpResponse(json.dumps({'url':img_url, 'name':img_name}))

def changeframe(request):
    print(request)
    params = json.loads(request.body.decode())
    print(params)
    img_name = ImageManager.changeframe(params)
    img_url = request._current_scheme_host + settings.MEDIA_URL + 'results/' + img_name
    print(img_url)
    return HttpResponse(json.dumps({'url':img_url, 'name':img_name}))

def delete(request, img_name):
    ImageManager.delete(img_name)
    return HttpResponse()

# class ImagesList(generics.ListCreateAPIView):
#     queryset = [ImageManager.objects.first()]
#     serializer_class = ImageManagerSerializer
