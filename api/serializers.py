from rest_framework import serializers

from .models import Espace, Chantier, Plage, Tache, Institution, Horaire, Pays, Region, Departement, Arrondissement, \
    Lampadaire  # noqa


class EspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espace
        fields = ('id', 'nom', 'adresse')


class PlageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plage
        fields = ('arrondissement_id', 'date', 'horaire_debut', 'horaire_fin')


class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = ('id', 'date', 'horaire_debut', 'horaire_fin', 'institution_id')


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'code')


class ChantierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chantier
        fields = ('id', 'espace')


class TacheSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tache
        fields = ('id', 'nom', 'etat', 'date_fin', 'chantier')


class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = ('id', 'code')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'code', 'pays_id')


class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departement
        fields = ('id', 'code', 'region_id')


class EspaceTravauxSerializer(serializers.ModelSerializer):
    dateFinTravaux = serializers.SerializerMethodField('_get_dateFinTravaux')

    class Meta:
        model = Espace
        fields = ('nom', 'adresse', 'dateFinTravaux')

    def _get_dateFinTravaux(self, obj):
        date_fin = None
        chantiers = Chantier.objects.filter(espace=obj)
        for chantier in chantiers:
            taches = Tache.objects.filter(chantier=chantier, date_fin__isnull=False)
            for tache in taches:
                if not date_fin or tache.date_fin > date_fin:
                    date_fin = tache.date_fin
        return date_fin


class EspaceTravauxOuvertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espace
        fields = '__all__'


class EclairageSerializer(serializers.ModelSerializer):
    plages = serializers.SerializerMethodField('_get_plages')

    class Meta:
        model = Lampadaire
        fields = ('id', 'latitude', 'longitude', 'plages')

    def _get_plages(self, obj):
        arrondissement = obj.arrondissement_id
        plages = Plage.objects.filter(arrondissement_id=arrondissement.id)

        return [{'Date': plage.date, 'Allumage': plage.horaire_debut, 'Extinction': plage.horaire_fin}
                for plage in plages]
