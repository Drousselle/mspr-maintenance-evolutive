from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.models import Region
from api.models import Departement
from api.models import Arrondissement
from api.views import ArrondissementViewSet
from api.serializers import ArrondissementSerializer


class GetArrondissement(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        pays_fr = Pays.objects.create(
            id="1", code="FR"
        )

        region_idf = Region.objects.create(
            id="1", code="IdF", pays_id=pays_fr
        )

        departement_paris = Departement.objects.create(
            id="1", code="PARIS", region_id=region_idf
        )

        Arrondissement.objects.create(
            id="1", code="01", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="2", code="02", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="3", code="03", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="4", code="04", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="5", code="05", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="6", code="06", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="7", code="07", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="8", code="08", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="9", code="09", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="10", code="10", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="11", code="11", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="12", code="12", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="13", code="13", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="14", code="14", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="15", code="15", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="16", code="16", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="17", code="17", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="18", code="18", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="19", code="19", departement_id=departement_paris
        )
        Arrondissement.objects.create(
            id="20", code="20", departement_id=departement_paris
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = ArrondissementViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_espaces(self):
        request = self.factory.get("")
        arrondissements = Arrondissement.objects.all()
        serializer = ArrondissementSerializer(arrondissements, many=True, context={'request': request})
        view = ArrondissementViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_espace(self):
        request = self.factory.get("")
        arrondissements = Arrondissement.objects.filter(id="7")
        serializer = ArrondissementSerializer(arrondissements, many=True, context={'request': request})
        view = ArrondissementViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="7")
        self.assertEqual(response.data, serializer.data[0])
