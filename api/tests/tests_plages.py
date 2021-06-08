from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.models import Region
from api.models import Departement
from api.models import Plage
from api.models import Arrondissement
from api.views import PlageViewSet
from api.serializers import PlageSerializer


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

        arrondissement_1 = Arrondissement.objects.create(
            id="1", code="01", departement_id=departement_paris
        )
        arrondissement_4 = Arrondissement.objects.create(
            id="4", code="04", departement_id=departement_paris
        )
        arrondissement_7 = Arrondissement.objects.create(
            id="7", code="07", departement_id=departement_paris
        )
        arrondissement_12 = Arrondissement.objects.create(
            id="12", code="12", departement_id=departement_paris
        )

        Plage.objects.create(
            id="1", arrondissement_id=arrondissement_1, date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="2", arrondissement_id=arrondissement_1, date="2021-06-07", horaire_debut="13:00", horaire_fin="17:00"
        )
        Plage.objects.create(
            id="3", arrondissement_id=arrondissement_1, date="2021-06-08", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="4", arrondissement_id=arrondissement_1, date="2021-06-08", horaire_debut="13:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="5", arrondissement_id=arrondissement_1, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="6", arrondissement_id=arrondissement_1, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="7", arrondissement_id=arrondissement_4, date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="8", arrondissement_id=arrondissement_4, date="2021-06-07", horaire_debut="13:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="9", arrondissement_id=arrondissement_4, date="2021-06-08", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="10", arrondissement_id=arrondissement_4, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="11", arrondissement_id=arrondissement_4, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="12", arrondissement_id=arrondissement_7, date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="13", arrondissement_id=arrondissement_7, date="2021-06-07", horaire_debut="12:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="14", arrondissement_id=arrondissement_7, date="2021-06-08", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="15", arrondissement_id=arrondissement_7, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="16", arrondissement_id=arrondissement_7, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="17", arrondissement_id=arrondissement_12, date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="18", arrondissement_id=arrondissement_12, date="2021-06-07", horaire_debut="09:00", horaire_fin="12:00"
        )
        Plage.objects.create(
            id="19", arrondissement_id=arrondissement_12, date="2021-06-08", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="20", arrondissement_id=arrondissement_12, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )
        Plage.objects.create(
            id="21", arrondissement_id=arrondissement_12, date="2021-06-10", horaire_debut="09:00", horaire_fin="16:00"
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = PlageViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_plages(self):
        request = self.factory.get("")
        plages = Plage.objects.all()
        serializer = PlageSerializer(plages, many=True)
        view = PlageViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_plage(self):
        request = self.factory.get("")
        plages = Plage.objects.filter(id="10")
        serializer = PlageSerializer(plages, many=True)
        view = PlageViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="10")
        self.assertEqual(response.data, serializer.data[0])