from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'espace', views.EspaceViewSet, 'espaces')
router.register(r'horaire', views.HoraireViewSet, 'horaires')
router.register(r'institution', views.InstitutionViewSet, 'institutions')
router.register(r'chantier', views.ChantierViewSet, 'chantiers')
router.register(r'tache', views.TacheViewSet, 'taches')
router.register(r'pays', views.PaysViewSet, 'pays')
router.register(r'region', views.RegionViewSet, 'regions')
router.register(r'departement', views.DepartementViewSet, 'departements')
router.register(r'eclairage', views.EclairageViewSet, 'eclairages')
router.register(r'espaces/travaux', views.EspacesTravauxViewSet, 'espaces_travaux')
router.register(r'espaces/ouverts', views.EspacesTravauxOuvertsViewSet, 'espaces_ouverts')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('eclairage/horaires/<str:date>/', views.GetEclairageByDay.as_view()),
    path('horaire/<str:codeInstitution>/<str:date>/', views.GetHoraireByInstitution.as_view())
]
