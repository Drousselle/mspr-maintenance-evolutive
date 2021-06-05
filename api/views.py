from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import EspaceSerializer
from .models import Espace


class EspaceViewSet(viewsets.ModelViewSet):
    queryset = Espace.objects.all().order_by('nom')
    serializer_class = EspaceSerializer
