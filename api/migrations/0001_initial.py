# Generated by Django 3.2.2 on 2021-06-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrondissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Chantier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Espace',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('adresse', models.CharField(max_length=200, verbose_name='Adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('code', models.CharField(max_length=20, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('etat', models.CharField(max_length=20, verbose_name='Nom')),
                ('date_fin', models.DateField(max_length=10, verbose_name='Date fin')),
                ('chantier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.chantier')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pays_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Lampadaire',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('latitude', models.FloatField(max_length=3, verbose_name='latitude')),
                ('longitude', models.FloatField(max_length=4, verbose_name='longitude')),
                ('arrondissement_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.arrondissement')),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.CharField(max_length=10, verbose_name='Debut')),
                ('fin', models.CharField(max_length=10, verbose_name='Fin')),
                ('institution_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.region')),
            ],
        ),
        migrations.AddField(
            model_name='chantier',
            name='espace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.espace'),
        ),
        migrations.AddField(
            model_name='arrondissement',
            name='departement_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.departement'),
        ),
    ]
