from rest_framework import serializers

from .models import Espace


class EspaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espace
        fields = ('id', 'nom', 'adresse')
