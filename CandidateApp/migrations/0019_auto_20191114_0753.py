# Generated by Django 2.2.6 on 2019-11-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0018_auto_20191114_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatecv',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
