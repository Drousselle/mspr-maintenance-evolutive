from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'espace', views.EspaceViewSet)
#router.register(r'horaire', views.HoraireViewSet)
#router.register(r'institution', views.InstitutionViewSet)
#router.register(r'chantier', views.ChantierViewSet)
#router.register(r'tache', views.TacheViewSet)
#router.register(r'pays', views.PaysViewSet)
#router.register(r'region', views.RegionViewSet)
#router.register(r'departement', views.DepartementViewSet)
router.register(r'eclairage/horaire', views.EclairageHoraireViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/<str:date>/', views.GetEclairageByDay.as_view())
]