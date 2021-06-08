from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.models import Region
from api.models import Plage
from api.models import Departement
from api.models import Arrondissement
from api.models import Lampadaire
from api.views import EclairageViewSet
from api.serializers import EclairageSerializer


class GetEclairages(TestCase):
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

        Lampadaire.objects.create(
            id="CD0X+32", latitude="-5.1", longitude="-68.3", arrondissement_id=arrondissement_1
        )
        Lampadaire.objects.create(
            id="CM1P-t2", latitude="-15.0", longitude="-68.3", arrondissement_id=arrondissement_1
        )
        Lampadaire.objects.create(
            id="AT43+V2", latitude="-12.1", longitude="8.8", arrondissement_id=arrondissement_4
        )
        Lampadaire.objects.create(
            id="B3GH-CD", latitude="-6.1", longitude="-78.3", arrondissement_id=arrondissement_7
        )
        Lampadaire.objects.create(
            id="AOP9+E4", latitude="7.03", longitude="-16.84", arrondissement_id=arrondissement_12
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = EclairageViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_eclaraiges(self):
        request = self.factory.get("")
        lampadaires = Lampadaire.objects.all()
        serializer = EclairageSerializer(lampadaires, many=True, context={'request': request})
        view = EclairageViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_eclairage(self):
        request = self.factory.get("")
        lampdaires = Lampadaire.objects.filter(id="CM1P-t2")
        serializer = EclairageSerializer(lampdaires, many=True, context={'request': request})
        view = EclairageViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="CM1P-t2")
        self.assertEqual(response.data, serializer.data[0])
