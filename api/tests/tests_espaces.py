from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Espace
from api.views import EspaceViewSet
from api.serializers import EspaceSerializer


class GetEspaces(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        Espace.objects.create(
            id='PLC_PIGALLE', nom='Place Pigalle', adresse='Place Pigalle 75009 PARIS'
        )
        Espace.objects.create(
            id='PRC_MONCEAU', nom='Parc Monceau', adresse='35 Boulevard de Courcelles, 75008 Paris'
        )
        Espace.objects.create(
            id='RUE_PELC', nom='Rue piétonne du Poil-au-con', adresse='Rue du Pélican 75001 PARIS'
        )
        Espace.objects.create(
            id='SLL_Z', nom='Salle Z', adresse='Plaque Télécom, Port Royal 74014 PARIS'
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = EspaceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_espaces(self):
        request = self.factory.get("")
        espaces = Espace.objects.all()
        serializer = EspaceSerializer(espaces, many=True)
        view = EspaceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_espace(self):
        request = self.factory.get("")
        espaces = Espace.objects.filter(id="PLC_PIGALLE")
        serializer = EspaceSerializer(espaces, many=True)
        view = EspaceViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="PLC_PIGALLE")
        self.assertEqual(response.data, serializer.data[0])
