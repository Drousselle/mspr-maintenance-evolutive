from django.db import models


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
    code = models.CharField('code', max_length=20)


class Horaire(models.Model):
    date = models.DateField('date', max_length=10)
    horaire_debut = models.CharField('Horaire debut', max_length=10)
    horaire_fin = models.CharField('Horaire fin', max_length=10)
    institution_id = models.ForeignKey(Institution, models.DO_NOTHING)


class Pays(models.Model):
    code = models.CharField('code', max_length=2)


class Region(models.Model):
    code = models.CharField('code', max_length=10)
    pays_id = models.ForeignKey(Pays, models.DO_NOTHING)


class Departement(models.Model):
    code = models.CharField('code', max_length=10)
    region_id = models.ForeignKey(Region, models.DO_NOTHING)


class Arrondissement(models.Model):
    code = models.CharField('code', max_length=10)
    departement_id = models.ForeignKey(Departement, models.DO_NOTHING)


class Plage(models.Model):
    arrondissement_id = models.ForeignKey(Arrondissement, models.DO_NOTHING)
    date = models.DateField('date', max_length=10)
    horaire_debut = models.CharField('heure debut', max_length=10)
    horaire_fin = models.CharField('heure fin', max_length=10)


class Lampadaire(models.Model):
    id = models.SlugField('Id', auto_created=False, unique=True, primary_key=True)
    latitude = models.FloatField('latitude', max_length=3)
    longitude = models.FloatField('longitude', max_length=4)
    arrondissement_id = models.ForeignKey(Arrondissement, models.DO_NOTHING)
