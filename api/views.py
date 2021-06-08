from .models import Espace, Chantier, Plage, Tache, Institution, Horaire, Pays, Region, Departement, Arrondissement, \
    Lampadaire  # noqa
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *  # noqa
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r


class ArrondissementViewSet(viewsets.ModelViewSet):
    queryset = Arrondissement.objects.all().order_by('id')
    serializer_class = ArrondissementSerializer # noqa
    http_method_names = ['get']


class EspaceViewSet(viewsets.ModelViewSet):
    queryset = Espace.objects.all().order_by('id')
    serializer_class = EspaceSerializer  # noqa
    http_method_names = ['get']


class HoraireViewSet(viewsets.ModelViewSet):
    queryset = Horaire.objects.all().order_by('institution_id')
    serializer_class = HoraireSerializer  # noqa
    http_method_names = ['get']


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all().order_by('id')
    serializer_class = InstitutionSerializer  # noqa
    http_method_names = ['get']


class PlageViewSet(viewsets.ModelViewSet):
    queryset = Plage.objects.all().order_by('id')
    serializer_class = PlageSerializer  # noqa
    http_method_names = ['get']


class ChantierViewSet(viewsets.ModelViewSet):
    queryset = Chantier.objects.all().order_by('id')
    serializer_class = ChantierSerializer  # noqa
    http_method_names = ['get']


class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all().order_by('id')
    serializer_class = TacheSerializer  # noqa
    http_method_names = ['get']


class PaysViewSet(viewsets.ModelViewSet):
    queryset = Pays.objects.all().order_by('id')
    serializer_class = PaysSerializer  # noqa
    http_method_names = ['get']


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('id')
    serializer_class = RegionSerializer  # noqa
    http_method_names = ['get']


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all().order_by('id')
    serializer_class = DepartementSerializer  # noqa
    http_method_names = ['get']


class EclairageViewSet(viewsets.ModelViewSet):
    queryset = Lampadaire.objects.all()
    serializer_class = EclairageSerializer  # noqa
    http_method_names = ['get']


class EspacesTravauxViewSet(viewsets.ModelViewSet):
    renderer_classes = (r.CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    espace_ids = []
    for espace in Espace.objects.all():
        for chantier in Chantier.objects.filter(espace=espace):
            taches = Tache.objects.filter(chantier=chantier)
            nb_done = taches.filter(etat='En cours')

            if len(nb_done) > 0:
                espace_ids.append(taches[0].chantier.espace.id)

    queryset = Espace.objects.filter(id__in=espace_ids).order_by('id')
    serializer_class = EspaceTravauxSerializer  # noqa
    http_method_names = ['get']


class EspacesTravauxOuvertsViewSet(viewsets.ModelViewSet):
    renderer_classes = (r.CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    espace_ids = []
    for espace in Espace.objects.all():
        for chantier in Chantier.objects.filter(espace=espace):
            taches = Tache.objects.filter(chantier=chantier)
            nb_done = taches.filter(etat='Terminée')

            if len(taches) == len(nb_done):
                espace_ids.append(taches[0].chantier.espace.id)

    queryset = Espace.objects.filter(id__in=espace_ids).order_by('id')
    serializer_class = EspaceTravauxOuvertsSerializer  # noqa
    http_method_names = ['get']


class GetEclairageByDay(APIView):

    def get(self, request, date):
        if len(date) != 8 or not date.isdecimal():
            return Response({"success": False, "content": "Date wrong format."})
        date = self._format_date(date)

        try:
            plages = Plage.objects.filter(date=date)
        except:  # noqa
            return Response({"success": False, "content": "Date wrong format."})
        if not plages:
            return Response({"success": False, "content": "No Schedule."})
        values = []
        for plage in plages:
            lampadaires = Lampadaire.objects.filter(arrondissement_id=plage.arrondissement_id)
            for lampadaire in lampadaires:
                values.append({'latitude': lampadaire.latitude,
                               'longitude': lampadaire.longitude,
                               'Allumage': plage.horaire_debut,
                               'Extinction': plage.horaire_fin})
        return Response(values)

    def _format_date(self, date):
        return '%s-%s-%s' % (date[4:8], date[2:4], date[:2])


class GetHoraireByInstitution(APIView):
    def get(self, request, codeInstitution, date):
        if len(date) != 8 or not date.isdecimal():
            return Response({"success": False, "content": "Date wrong format."})

        date = self._format_date(date)
        try:
            horaires = Horaire.objects.filter(date=date, institution_id__code=codeInstitution)
        except:  # noqa
            return Response({"success": False, "content": "Date wrong format."})
        if not horaires:
            return Response({"success": False, "content": "No Schedule."})
        return Response([{'heureOuverture': horaire.horaire_debut, 'heureFermeture': horaire.horaire_fin}
                         for horaire in horaires])

    def _format_date(self, date):
        return '%s-%s-%s' % (date[4:8], date[2:4], date[:2])
