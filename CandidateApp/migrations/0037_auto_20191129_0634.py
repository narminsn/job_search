# Generated by Django 2.2.6 on 2019-11-29 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0036_auto_20191129_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepost',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 29, 6, 34, 55, 395266)),
        ),
    ]
