from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Pays
from api.views import PaysViewSet
from api.serializers import PaysSerializer


class GetPays(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        Pays.objects.create(
            id="1", code="FR"
        )
        Pays.objects.create(
            id="2", code="BE"
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = PaysViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_pays(self):
        request = self.factory.get("")
        pays = Pays.objects.all()
        serializer = PaysSerializer(pays, many=True)
        view = PaysViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_pays(self):
        request = self.factory.get("")
        pays = Pays.objects.filter(id="2")
        serializer = PaysSerializer(pays, many=True)
        view = PaysViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="2")
        self.assertEqual(response.data, serializer.data[0])
