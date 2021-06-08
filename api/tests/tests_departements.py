from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.models import Region
from api.models import Departement
from api.views import DepartementViewSet
from api.serializers import DepartementSerializer


class GetRegions(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        pays_fr = Pays.objects.create(
            id="1", code="FR"
        )
        pays_be = Pays.objects.create(
            id="2", code="BE"
        )

        region_idf = Region.objects.create(
            id="1", code="IdF", pays_id=pays_fr
        )
        region_bc = Region.objects.create(
            id="2", code="BC", pays_id=pays_be
        )

        Departement.objects.create(
            id="1", code="PARIS", region_id=region_idf
        )
        Departement.objects.create(
            id="2", code="BRUXELLES", region_id=region_bc
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = DepartementViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_departements(self):
        request = self.factory.get("")
        departements = Departement.objects.all()
        serializer = DepartementSerializer(departements, many=True, context={'request': request})
        view = DepartementViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_departement(self):
        request = self.factory.get("")
        departements = Departement.objects.filter(id="1")
        serializer = DepartementSerializer(departements, many=True, context={'request': request})
        view = DepartementViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="1")
        self.assertEqual(response.data, serializer.data[0])