from django.db import models


# Create your models here.

class Espace(models.Model):
    id = models.SlugField('Id', auto_created=False, unique=True, primary_key=True)
    nom = models.CharField('Nom', max_length=50)
    adresse = models.CharField('Adresse', max_length=200)


class Chantier(models.Model):
    espace = models.ForeignKey(Espace, models.DO_NOTHING)


class Tache(models.Model):
    nom = models.CharField('Nom', max_length=50)
    etat = models.CharField('Nom', max_length=20)
    date_fin = models.DateField('Date fin', max_length=10)
    chantier = models.ForeignKey('Chantier', models.DO_NOTHING)


class Institution(models.Model):
    id = models.SlugField('Id', auto_created=False, unique=True, primary_key=True)
    code = models.CharField('code', max_length=20)


class Horaire(models.Model):
    debut = models.CharField('Debut', max_length=10)
    fin = models.CharField('Fin', max_length=10)
    institution_id = models.ForeignKey(Institution, models.DO_NOTHING)


class Pays(models.Model):
    code = models.CharField('code', max_length=2)


class Region(models.Model):
    pays_id = models.ForeignKey(Pays, models.DO_NOTHING)


class Departement(models.Model):
    region_id = models.ForeignKey(Region, models.DO_NOTHING)


class Arrondissement(models.Model):
    departement_id = models.ForeignKey(Departement, models.DO_NOTHING)


class Lampadaire(models.Model):
    id = models.SlugField('Id', auto_created=False, unique=True, primary_key=True)
    latitude = models.FloatField('latitude', max_length=3)
    longitude = models.FloatField('longitude', max_length=4)
    arrondissement_id = models.ForeignKey(Arrondissement, models.DO_NOTHING)
