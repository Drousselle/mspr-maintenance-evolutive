from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Chantier
from api.models import Espace
from api.views import ChantierViewSet
from api.serializers import ChantierSerializer

class GetChantier(TestCase):
    """
    """

    factory = APIRequestFactory()

    def setUp(self):
        espace_pigalle = Espace.objects.create(
            id='PLC_PIGALLE', nom='Place Pigalle', adresse='Place Pigalle 75009 PARIS'
        )
        espace_monceau = Espace.objects.create(
            id='PRC_MONCEAU', nom='Parc Monceau', adresse='35 Boulevard de Courcelles, 75008 Paris'
        )
        espace_pelc = Espace.objects.create(
            id='RUE_PELC', nom='Rue piétonne du Poil-au-con', adresse='Rue du Pélican 75001 PARIS'
        )
        espace_salle = Espace.objects.create(
            id='SLL_Z', nom='Salle Z', adresse='Plaque Télécom, Port Royal 74014 PARIS'
        )

        Chantier.objects.create(
            id='1', espace=espace_pigalle
        )
        Chantier.objects.create(
            id='2', espace=espace_monceau
        )
        Chantier.objects.create(
            id='3', espace=espace_pelc
        )
        Chantier.objects.create(
            id='4', espace=espace_salle
        )

    def test_http_code_200(self):
        request = self.factory.get('/api/chantier/')
        view = ChantierViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_chantiers(self):
        request = self.factory.get('/api/chantier/')
        chantiers = Chantier.objects.all()
        serializer = ChantierSerializer(chantiers, many=True)
        view = ChantierViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_chantier(self):
        request = self.factory.get('/api/chantier/')
        chantiers = Chantier.objects.filter(id="3")
        serializer = ChantierSerializer(chantiers, many=True)
        view = ChantierViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="3")
        self.assertEqual(response.data, serializer.data[0])