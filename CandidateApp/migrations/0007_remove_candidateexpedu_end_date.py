# Generated by Django 2.2.6 on 2019-11-05 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0006_auto_20191105_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateexpedu',
            name='end_date',
        ),
    ]
