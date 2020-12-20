# views.py
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework import permissions
from rentsites.models import Rentsite
from rentsites.serializers import RentsitesSerializer
#from collections import OrderedDict
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend



def index(request):
    return render(request, template_name='index.html')


def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'You get an phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
        ]
    })
    return response

class RentsitesViewSet(viewsets.ModelViewSet):
    queryset = Rentsite.objects.all()
    serializer_class = RentsitesSerializer
