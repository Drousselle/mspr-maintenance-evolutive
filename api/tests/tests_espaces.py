from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Espace
from api.views import EspaceViewSet
from api.serializers import EspaceSerializer


class GetAllEspaces(TestCase):
    """
    """

    factory = APIRequestFactory()

    def setUp(self):
        Espace.objects.create(
            id='PLC_PIGALLE', nom='Place Pigalle', adresse='Place Pigalle 75009 PARIS')
        Espace.objects.create(
            id='PRC_MONCEAU', nom='Parc Monceau', adresse='35 Boulevard de Courcelles, 75008 Paris')
        Espace.objects.create(
            id='RUE_PELC', nom='Rue piétonne du Poil-au-con', adresse='Rue du Pélican 75001 PARIS')

    def test_http_code_200(self):
        request = self.factory.get('/api/espace/')
        view = EspaceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_espaces(self):
        request = self.factory.get('/api/espace/')
        espaces = Espace.objects.all()
        serializer = EspaceSerializer(espaces, many=True)
        view = EspaceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(len(response.data), len(serializer.data))