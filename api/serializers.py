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
    pays_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Region
        fields = ('id', 'pays_id')


class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    region_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Departement
        fields = ('id', 'region_id')


class PlageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plage
        fields = ('date', 'horaire_debut', 'horaire_fin')


class LampadaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lampadaire
        fields = ('latitude', 'longitude')


class EclairageHoraireSerialize(serializers.ModelSerializer):
    lampadaire_set = LampadaireSerializer(many=True, read_only=True)
    plage_set = PlageSerializer(many=True, read_only=True)

    class Meta:
        model = Arrondissement
        fields = ('id', 'lampadaire_set', 'plage_set')


class ArrondissementSerializer(serializers.ModelSerializer):
    lampadaire_set = LampadaireSerializer(many=True, read_only=True)
    plage_set = PlageSerializer(many=True, read_only=True)

    class Meta:
        model = Arrondissement
        fields = ('id', 'lampadaire_set', 'plage_set')

