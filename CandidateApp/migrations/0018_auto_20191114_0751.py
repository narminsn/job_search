# Generated by Django 2.2.6 on 2019-11-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0017_candidatecv_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatecv',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
