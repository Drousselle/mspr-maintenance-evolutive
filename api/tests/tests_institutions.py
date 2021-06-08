from rest_framework.test import APIRequestFactory
from django.test import TestCase
from api.models import Institution
from api.views import InstitutionViewSet
from api.serializers import InstitutionSerializer


class getInstitution(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        Institution.objects.create(
            id="1", code="POSTE_CHATELET"
        )
        Institution.objects.create(
            id="2", code="POSTE_ARRAS"
        )

    def test_http_code_200(self):
        request = self.factory.get("")
        view = InstitutionViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_all_institutions(self):
        request = self.factory.get("")
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        view = InstitutionViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data, serializer.data)

    def test_get_one_institution(self):
        request = self.factory.get("")
        institutions = Institution.objects.filter(id="1")
        serializer = InstitutionSerializer(institutions, many=True)
        view = InstitutionViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk="1")
        self.assertEqual(response.data, serializer.data[0])