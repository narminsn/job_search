# Generated by Django 2.2.6 on 2019-11-03 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CityModel',
        ),
        migrations.DeleteModel(
            name='CountryModel',
        ),
    ]
