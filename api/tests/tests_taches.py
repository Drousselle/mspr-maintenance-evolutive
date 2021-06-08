from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Tache
from api.models import Chantier
from api.models import Espace
from api.views import TacheViewSet
from api.serializers import TacheSerializer


class GetChantiers(TestCase):
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

        chantier_1 = Chantier.objects.create(
            id='1', espace=espace_pigalle
        )
        chantier_2 = Chantier.objects.create(
            id='2', espace=espace_monceau
        )
        chantier_3 = Chantier.objects.create(
            id='3', espace=espace_pelc
        )
        chantier_4 = Chantier.objects.create(
            id='4', espace=espace_salle
        )

        Tache.objects.create(
            id='1', nom='Terrassement', etat='Terminée', date_fin='1986-02-16', chantier=chantier_1
        )
        Tache.objects.create(
            id='2', nom='Expertise circulation', etat='En cours', date_fin='1986-02-16', chantier=chantier_1
        )
        Tache.objects.create(
            id='3', nom='Installation sapin de Noël', etat='Terminée', date_fin='1986-02-16', chantier=chantier_1
        )
        Tache.objects.create(
            id='4', nom='Pose isolant mousse', etat='Terminée', date_fin='1977-02-16', chantier=chantier_2
        )
        Tache.objects.create(
            id='5', nom='Toitures kiosques', etat='Terminée', date_fin='1977-02-16', chantier=chantier_2
        )
        Tache.objects.create(
            id='6', nom='Terrassement', etat='Terminée', date_fin='1995-02-01', chantier=chantier_3
        )
        Tache.objects.create(
            id='7', nom='Réfection pavés', etat='Terminée', date_fin='1998-08-10', chantier=chantier_3
        )
        Tache.objects.create(
            id='8', nom='Déblaiement', etat='Terminée', date_fin='1960-02-16', chantier=chantier_4
        )
        Tache.objects.create(
            id='9', nom='Évacuation caddies', etat='Terminée', date_fin='2009-06-11', chantier=chantier_4
        )
        Tache.objects.create(
            id='10', nom='Évacuation caddies', etat='Terminée', date_fin='2001-11-10', chantier=chantier_4
        )
        Tache.objects.create(
            id='11', nom='Évacuation caddies', etat='Terminée', date_fin='2002-07-03', chantier=chantier_4
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = TacheViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_tachees(self):
        request = self.factory.get("")
        taches = Tache.objects.all()
        serializer = TacheSerializer(taches, many=True, context={'request': request})
        view = TacheViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_tache(self):
        request = self.factory.get("")
        taches = Tache.objects.filter(id="5")
        serializer = TacheSerializer(taches, many=True, context={'request': request})
        view = TacheViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="5")
        self.assertEqual(response.data, serializer.data[0])