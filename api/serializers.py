from rest_framework import serializers

from .models import *


class EspaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espace
        fields = ('id', 'nom', 'adresse')


class HoraireSerializer(serializers.HyperlinkedModelSerializer):
    # Affiche l'ID de l'institution dans l'api au lieu du lien vers celle-ci
    # institution_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Horaire
        fields = ('institution_id', 'debut', 'fin')


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'code')


class ChantierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chantier
        fields = ('id', 'espace')


class TacheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tache
        fields = ('nom', 'etat', 'date_fin', 'chantier')


class PaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pays
        fields = ('id', 'code')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'pays_id')


class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departement
        fields = ('id', 'region_id')


class ArrondissementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arrondissement
        fields = ('id', 'departement_id')


class PlageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plage
        fields = ('arrondissement_id', 'horaire_debut', 'horaire_fin')


class LampadaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lampadaire
        fields = ('id', 'latitude', 'longitude', 'arrondissement_id')
