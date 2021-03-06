# Generated by Django 3.2.4 on 2021-06-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plage',
            name='date',
            field=models.DateField(max_length=10, verbose_name='date'),
        ),
        migrations.AlterUniqueTogether(
            name='plage',
            unique_together={('arrondissement_id', 'date')},
        ),
    ]
