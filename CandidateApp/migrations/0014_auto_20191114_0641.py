# Generated by Django 2.2.6 on 2019-11-14 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0013_auto_20191114_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatecv',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
