# Generated by Django 3.2.2 on 2021-06-05 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_date_debut_plage_horaire_debut'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plage',
            old_name='date_fin',
            new_name='horaire_fin',
        ),
    ]
