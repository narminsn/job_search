# Generated by Django 2.2.6 on 2019-11-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0016_aboutcomp'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcomp',
            name='experience',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
