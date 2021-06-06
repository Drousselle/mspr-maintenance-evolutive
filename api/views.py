from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class EspaceViewSet(viewsets.ModelViewSet):
    queryset = Espace.objects.all().order_by('nom')
    serializer_class = EspaceSerializer


class HoraireViewSet(viewsets.ModelViewSet):
    queryset = Horaire.objects.all().order_by('institution_id')
    serializer_class = HoraireSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all().order_by('id')
    serializer_class = InstitutionSerializer


class ChantierViewSet(viewsets.ModelViewSet):
    queryset = Chantier.objects.all().order_by('id')
    serializer_class = ChantierSerializer


class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all().order_by('id')
    serializer_class = TacheSerializer


class PaysViewSet(viewsets.ModelViewSet):
    queryset = Pays.objects.all().order_by('id')
    serializer_class = PaysSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('id')
    serializer_class = RegionSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all().order_by('id')
    serializer_class = DepartementSerializer


class EclairageHoraireViewSet(viewsets.ModelViewSet):
    queryset = Lampadaire.objects.all()
    serializer_class = EclairageHoraireSerializer


class GetEclairageByDay(APIView):

    def get(self, request, date):
        """
        """
        print('____________________ ')
        print(self)
        print(request)
        print(date)
        return Response({"success": True, "content": "Hello World!"})