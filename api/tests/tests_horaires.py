from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Horaire
from api.models import Institution
from api.views import HoraireViewSet
from api.serializers import HoraireSerializer


class getHoraire(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        institution_1 = Institution.objects.create(id="1", code="POSTE_CHATELET")
        institution_2 = Institution.objects.create(id="2", code="POSTE_ARRAS")
        Horaire.objects.create(
            id="1", date="2021-06-08", horaire_debut="09:00", horaire_fin="17:00", institution_id=institution_1
        )
        Horaire.objects.create(
            id="2", date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00", institution_id=institution_2
        )
        Horaire.objects.create(
            id="3", date="2021-06-07", horaire_debut="13:00", horaire_fin="18:00", institution_id=institution_2
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = HoraireViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_horaires(self):
        request = self.factory.get("")
        horaires = Horaire.objects.all()
        serializer = HoraireSerializer(horaires, many=True)
        view = HoraireViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_horaire(self):
        request = self.factory.get("")
        horaires = Horaire.objects.filter(id="2")
        serializer = HoraireSerializer(horaires, many=True)
        view = HoraireViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="2")
        self.assertEqual(response.data, serializer.data[0])
