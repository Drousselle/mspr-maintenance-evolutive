from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.models import Region
from api.views import RegionViewSet
from api.serializers import RegionSerializer


class GetRegions(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        pays_fr = Pays.objects.create(
            id="1", code="FR"
        )
        pays_be = Pays.objects.create(
            id="2", code="BE"
        )

        Region.objects.create(
            id="1", code="IdF", pays_id=pays_fr
        )
        Region.objects.create(
            id="2", code="BC", pays_id=pays_be
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = RegionViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_regions(self):
        request = self.factory.get("")
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        view = RegionViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_region(self):
        request = self.factory.get("")
        regions = Region.objects.filter(id="1")
        serializer = RegionSerializer(regions, many=True)
        view = RegionViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="1")
        self.assertEqual(response.data, serializer.data[0])
