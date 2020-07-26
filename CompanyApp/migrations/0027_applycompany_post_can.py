# Generated by Django 2.2.6 on 2019-11-29 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0035_auto_20191129_0631'),
        ('CompanyApp', '0026_remove_applycompany_post_can'),
    ]

    operations = [
        migrations.AddField(
            model_name='applycompany',
            name='post_can',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CandidateApp.CandidatePost'),
        ),
    ]
